from formulae import decision_probability


def nothing(i, g, v):
    """ Logs nothing. """


def iteration(i, g, v):
    """ Logs only current iteration. """

    print('Iteration:   ', i)


def average(i, g, v):
    """ Logs average preference density. """

    m = g.nodes                                           # Members.
    w = {m: g.nodes[m]['w'] for m in m}                   # Densities.
    a = {v: sum(w[m](v) for m in m) / len(m) for v in v}  # Average.

    print('Iteration:   ', i)
    print('   ', 'Average density:', a)


def everything(i, g, v):
    """ Logs average density and density of each member. """

    m = g.nodes                                           # Members.
    w = {m: g.nodes[m]['w'] for m in m}                   # Densities.
    a = {v: sum(w[m](v) for m in m) / len(m) for v in v}  # Average.

    print('Iteration:   ', i)
    print('   ', 'Average density:', a)
    print()

    for m, data in g.nodes(data=True):
        mw = data['w']
        mrho = data['rho']

        print('   ', m,
              {v: mw(v) for v in v},
              {j: decision_probability(j, v, mw, mrho) for j in v.union({0})})

    print()
