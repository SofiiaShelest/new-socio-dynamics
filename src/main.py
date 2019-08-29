import log
import plot
import simulation
import formulae

from common import measure
from experiments import three_leaders


def main(**kwargs):
    v = {-1, +1, +2}  # Set of votes.
    n = 5000      # Number of iterations.

    g = three_leaders(v)

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
        colours = {-1: 'r', 0: 'g', +1: 'b', +2: 'y'}
        cesaro = {x: formulae.cesaro(y) for x, y in measures.items()}

        plot.lines(measures, colours)
        plot.lines(cesaro, colours)

        plot.show()


if __name__ == '__main__':
    # Run `main` and measure its execution time.
    elapsed = measure(lambda: main(log=log.everything, plot=True))

    print()
    print('Elapsed:', elapsed, 'seconds.')
