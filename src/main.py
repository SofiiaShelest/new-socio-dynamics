import networkx as nx
import initialise
import log
import simulation

from common import measure


def main(**kwargs):
    v = {-1, +1}  # Set of votes.
    n = 300       # Number of iterations.

    g = nx.newman_watts_strogatz_graph(500, k=10, p=0.7)

    initialise.edges(g, a=lambda: 0.3)
    initialise.nodes(g, v, rho=lambda: 25)

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
