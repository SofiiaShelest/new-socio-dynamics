import math
import numpy


def normalised_entropy(v, w):
    """
    Computes the normalised entropy of a preference density function `w`
    over a set of votes `v`.

    :param v: Set of votes `V` (excluding 0).
    :param w: Preference density function.
    :return: Normalised entropy.
    """

    assert 0 not in v
    assert len(v) > 0

    log = math.log2
    m = len(v)

    return (-1 / log(m)) * sum(w(v) * log(w(v)) for v in v)


def decision_probability(j, v, w, ro):
    """
    Computes the probability of a vote `j` to be a decision of a member.

    :param j: Vote from `V + {0}`.
    :param v: Set of votes `V` (excluding 0).
    :param w: Preference density function.
    :param ro: Impulsiveness indicator.
    :return: Probability from range [0, 1].
    """

    assert j == 0 or j in v
    assert 0 not in v
    assert ro > 0

    h = normalised_entropy

    if j == 0:
        return h(v, w) ** ro
    else:
        return (1 - h(v, w) ** ro) * w(j)


def decision(v, w, ro):
    """
    Computes the decision of a member during a communication
    depending on a preference density function `w`.

    :param v: Set of votes `V` (excluding 0).
    :param w: Preference density function.
    :param ro: Impulsiveness indicator.
    :return: Decision of the member.
    """

    assert 0 not in v
    assert ro > 0

    v = list(v)  # Fix the order.
    p = [decision_probability(j, v, w, ro) for j in v + [0]]

    return numpy.random.choice(v + [0], p=p)


def valuation_density(g, m, n):
    """
    Computes the valuation preference density `w[m, n](v)`.

    :param g: Graph `G = (M, C)`.
    :param m: Member from the set `M`.
    :param n: Member from the set `M`.
    :return: Valuation preference density.
    """

    assert m is not n
    assert m in g.nodes and n in g.nodes

    wm = g.nodes[m]['w']  # Preference density function of the member `m`.
    wn = g.nodes[n]['w']  # Preference density function of the member `n`.

    d = g.edges[m, n]['d']  # Dialogue matrix.

    # Valuation preference density.
    def w(v):
        a = min  # Alice.
        b = max  # Bob.

        if m == a({m, n}):
            return \
                (d[0, 0] + d[0, 1]) * wm(v) + \
                (d[1, 0] + d[1, 1]) * wn(v)

        if m == b({m, n}):
            return \
                (d[0, 1] + d[1, 1]) * wm(v) + \
                (d[0, 0] + d[1, 0]) * wn(v)

    return w


def average_density(m, i, w):
    """
    Computes the average preference density of the member `m`
    immediately after a communication session.

    :param m: Member from the set `M`.
    :param i: Active neighbours.
    :param w: Valuation preference densities.
    :return: Average preference density.
    """

    return \
        lambda v: (1 / len(i[m])) * sum(w[m, n](v) for n in i[m])


def occupation_measure(g, j):
    """
    Computes the current occupation measure.

    :param g: Graph `G = (M, C)`.
    :param j: Vote from `V + {0}`.
    :return: Occupation measure.
    """

    m = g.nodes                    # Members.
    d = lambda n: g.nodes[n]['d']  # Decision of a member `n`.

    return (1 / len(m)) * sum(d(m) == j for m in m)
