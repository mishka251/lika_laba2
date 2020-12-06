
from input_data import variant2
from solvers import GradientSolver, GradientSplitSolver, CoordsSolver, Evristic, ConfigurationsConst, Simplex
import numpy as np
import matplotlib.pyplot as plt

solvers = [
    GradientSolver(alpha=0.3),
    GradientSplitSolver(alpha=0.3),
    CoordsSolver(alpha=0.3),
    #Evristic(0.3, 0.3),
    ConfigurationsConst(0.5, 1e-4, 0.1),
    Simplex(0.5),
]

@np.vectorize
def f(x1, x2):
    return variant2.function(x1, x2)

for solver in solvers:
    fig = plt.figure()
    ax = fig.gca(projection='3d')


    res = solver(variant2)
    print(res)
    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    Z = f(X,Y)

    surf = ax.plot_surface(X, Y, Z,
                           linewidth=0, antialiased=False, alpha=0.5)


    l_x = [x[0] for x in res.path]
    l_y = [x[1] for x in res.path]
    l_z = [variant2.function(x, y) for (x, y) in res.path]
    ax.plot(l_x, l_y, l_z, label='path')
    ax.set_xlim(min(l_x)-1, max(l_x)+1)
    ax.set_ylim(min(l_y) - 1, max(l_y) + 1)

    #plt.show()
    plt.savefig(res.method+'.jpg')
    plt.clf()
