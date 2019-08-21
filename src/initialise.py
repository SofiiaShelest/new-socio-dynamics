from numpy.random import uniform

from common import function
from formulae import decision


def nodes(g, v, rho):
    """
    Initialises attributes of the nodes of the graph `g`:
        - 'w' for preference density function;
        - 'd' for initial decision of a member;
        - 'rho' for impulsiveness indicator.

    :param g: Graph.
    :param v: Set of votes `V` (excluding 0).
    :param rho: Function that returns impulsiveness indicator.

    Examples:
        nodes(g, v, rho=lambda: 25)
        nodes(g, v, rho=lambda: uniform(20, 30))
    """

    for _, data in g.nodes(data=True):
        w = {v: int(uniform() * 10000) for v in v}
        w = {v: w[v] / sum(w.values()) for v in v}
        w = function(w)

        data['w'] = w  # Preference density function.
        data['rho'] = rho()  # Impulsiveness indicator.
        data['d'] = decision(v, data['w'], data['rho'])  # Initial decision.

        assert sum(w(v) for v in v) == 1
        assert all(w(v) > 0 for v in v)
        assert data['rho'] > 0
        assert data['d'] == 0 or data['d'] in v


def edges(g, a):
    """
    Initialises attributes of the edges of the graph `g`:
        - 'a' for activation ratio;
        - 'd' for dialogue matrix.

    :param g: Graph.
    :param a: Function that returns activation ratio.

    Examples:
        edges(g, a=lambda: 0.5)
        edges(g, a=lambda: uniform(0.3, 0.7))
    """

    for _, _, data in g.edges(data=True):
        x = [int(uniform() * 10000) for _ in range(4)]

        data['a'] = a()             # Activation ratio.
        data['d'] = {               # Dialogue matrix.
            (0, 0): x[0] / sum(x),
            (0, 1): x[1] / sum(x),
            (1, 0): x[2] / sum(x),
            (1, 1): x[3] / sum(x),
        }

        assert 0 <= data['a'] <= 1


def leader(g, v, m, j):
    """
    Makes a leader out of the member.

    :param g: Graph.
    :param v: Set of votes `V` (excluding 0).
    :param m: The node that will become a leader.
    :param j: Vote of the leader.
    """

    w = {v: uniform(0.001, 0.002) for v in v}
    w[j] = 1 - sum(w.values()) + w[j]
    w = function(w)

    data = g.nodes[m]
    data['w'] = w  # Preference density function.
    data['d'] = decision(v, data['w'], data['rho'])  # Initial decision.

    for n in g.neighbors(m):
        r = uniform(0, 0.5)

        data = g.edges[m, n]
        data['d'] = {       # Dialogue matrix.
            (0, 0): r,
            (0, 1): 1 - r,
            (1, 0): 0,
            (1, 1): 0,
        }
