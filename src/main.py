import networkx as nx
from numpy.random.mtrand import uniform

import initialise
import log
import simulation

from common import measure


def main(**kwargs):
    v = {-1, +1}  # Set of votes.
    n = 300       # Number of iterations.

    g = nx.complete_graph(50)

    initialise.nodes(g, v, ro=lambda: 1)
    initialise.edges(g, a=lambda: 1.0)
    initialise.leader(g, 0, r=uniform(0, 0.5))

    # Main cycle.
    for i in range(n):
        simulation.iteration(g, v)

        # Logging.
        if 'log' in kwargs:
            kwargs['log'](i, g, v)


if __name__ == '__main__':
    # Run `main` and measure its execution time.
    elapsed = measure(lambda: main(log=log.nothing))

    print()
    print('Elapsed:', elapsed, 'seconds.')
