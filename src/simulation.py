import numpy
import functools

from formulae import valuation_density, average_density, decision


def trial(p):
    """
    Bernoulli trial with probability of `p`.

    :param p: Probability from range [0, 1].
    :return: Boolean value depending on the outcome of the trial:
        - `True` if outcome is positive;
        - `False` if outcome is negative.

    >>> import numpy as np

    >>> np.random.seed(1984)
    >>> sum(trial(0.3) for _ in range(1000)) / 1000
    0.303

    >>> np.random.seed(451)
    >>> sum(trial(0.8) for _ in range(1000)) / 1000
    0.811
    """

    assert 0 <= p <= 1

    return numpy.random.uniform() < p


def neighbours(m, c):
    """
    Returns a set of neighbours of the specified member `m`
    depending on the set of channels `c`.

    :param m: Member neighbours of which should be computed.
    :param c: Set of channels.
    :return: Set of neighbours.

    >>> neighbours(1, {})
    set()

    >>> neighbours(1, {(2, 1)})
    {2}

    >>> neighbours(1, {(1, 2), (3, 1), (4, 5)})
    {2, 3}
    """

    return {x for x, y in c if y == m}.union(
           {y for x, y in c if x == m})


def iteration(g, v):
    """
    Performs a single iteration of the simulation.

    :param g: Graph `G = (M, C)`.
    :param v: Set of votes `V` (excluding 0).
    """

    # Activation ratio of a channel `x`.
    def a(x):
        return g.edges[x]['a']

    c = {c for c in g.edges if trial(a(c))}     # Active channels.
    i = {m: neighbours(m, c) for m in g.nodes}  # Active neighbours.

    w = {(m, n): valuation_density(g, m, n)
         for m in g.nodes
         for n in i[m]}

    for m, data in g.nodes(data=True):
        if len(i[m]) == 0:
            # Skip members that did not have active
            # neighbours to communicate with.
            continue

        # Optimisation to prevent multiple evaluations.
        cached = functools.lru_cache(maxsize=len(v))

        data['w'] = cached(average_density(m, i, w))
        data['d'] = decision(v, data['w'], data['ro'])
