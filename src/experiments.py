import networkx as nx
from numpy.random.mtrand import uniform

import initialise


def one_leader(votes, ):
    g = nx.complete_graph(50)

    initialise.nodes(g, votes, rho=lambda: 1)
    initialise.edges(g, a=lambda: 1.0)
    initialise.leader(g, votes, m=0, j=-1)

    return g


def two_leaders(votes):
    g = nx.complete_graph(50)

    initialise.nodes(g, votes, rho=lambda: 1)
    initialise.edges(g, a=lambda: 1.0)
    initialise.leader(g, votes, m=0, j=-1)
    initialise.leader(g, votes, m=1, j=1)

    g.remove_edge(0, 1)

    return g


def three_leaders(votes):
    g = nx.complete_graph(50)

    initialise.nodes(g, votes, rho=lambda: 1)
    initialise.edges(g, a=lambda: 1)
    initialise.leader(g, votes, m=0, j=-1, a=lambda: 0.8)
    initialise.leader(g, votes, m=1, j=1, a=lambda: 0.6)
    initialise.leader(g, votes, m=2, j=2, a=lambda: 0.4)

    g.remove_edge(0, 1)
    g.remove_edge(1, 2)
    g.remove_edge(2, 0)

    return g
