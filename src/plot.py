import matplotlib.pyplot as plt


def occupation_measures(m, colours=None):
    """
    Plots occupation measures.

    :param m: Computed occupation measures ({j: measure[i]}, `j` from V + {0}).
    :param colours: Dictionary of colours for `j` from V + {0}.
    """

    colours = colours or {}

    for j in m:
        if j in colours:
            plt.plot(m[j], color=colours[j])
        else:
            plt.plot(m[j])


def show():
    """
    Shows drawn plots.
    """

    plt.show()
