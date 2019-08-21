import matplotlib.pyplot as plt


def lines(m, colours=None):
    """ Draws multiple plots.

    :param m: Dictionary of lines to draw ({x: line}).
    :param colours: Dictionary of colours ({x: colour}).
    """

    colours = colours or {}

    plt.figure()

    for j in m:
        if j in colours:
            plt.plot(m[j], color=colours[j])
        else:
            plt.plot(m[j])


def show():
    """ Shows drawn plots. """

    plt.show()
