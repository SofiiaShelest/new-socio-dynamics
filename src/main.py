import networkx as nx
from numpy.random.mtrand import uniform

import initialise
import log
import plot
import simulation
import formulae

from common import measure


def main(**kwargs):
    v = {-1, +1}  # Set of votes.
    n = 1000      # Number of iterations.

    g = nx.complete_graph(50)

    initialise.nodes(g, v, rho=lambda: 1)
    initialise.edges(g, a=lambda: 1.0)
    initialise.leader(g, v, m=0, j=-1, r=lambda: uniform(0, 0.5))

    measures = {j: [] for j in v.union({0})}
    
    # Main cycle.
    for i in range(n):
        simulation.iteration(g, v)

        for j in v.union({0}):
            measures[j].append(formulae.occupation_measure(g, j))

        # Log.
        if 'log' in kwargs:
            kwargs['log'](i, g, v)

    # Plot.
    if kwargs.get('plot', False):
        colours = {-1: 'r', 0: 'g', +1: 'b'}
        cesaro = {x: formulae.cesaro(y) for x, y in measures.items()}

        plot.lines(measures, colours)
        plot.lines(cesaro, colours)

        plot.show()


if __name__ == '__main__':
    # Run `main` and measure its execution time.
    elapsed = measure(lambda: main(log=log.everything, plot=True))

    print()
    print('Elapsed:', elapsed, 'seconds.')
