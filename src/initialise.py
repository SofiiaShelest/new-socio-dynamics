from numpy.random import uniform

from common import function
from formulae import decision


def nodes(g, v, ro):
    """
    Initialises attributes of the nodes of the graph `g`:
        - 'w' for preference density function;
        - 'd' for initial decision of a member;
        - 'ro' for impulsiveness indicator.

    :param g: Graph.
    :param v: Set of votes `V` (excluding 0).
    :param ro: Function that returns impulsiveness indicator.

    Examples:
        nodes(g, v, ro=lambda: 25)
        nodes(g, v, ro=lambda: uniform(20, 30))
    """

    for _, data in g.nodes(data=True):
        # Preference density function.
        x = [int(uniform() * 10000) for _ in v]

        w = {v: x[i] / sum(x) for i, v in enumerate(v)}
        w = function(w)

        data['w'] = w

        data['ro'] = ro()  # Impulsiveness indicator.
        data['d'] = decision(v, data['w'], data['ro'])  # Initial decision.

        assert sum(w(v) for v in v) == 1
        assert data['ro'] > 0
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
        edges(g, a=lambda: uniform(0.3, 0.7)
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
