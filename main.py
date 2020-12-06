
from input_data import variant2
from solvers import GradientSolver, GradientSplitSolver, CoordsSolver, Evristic, ConfigurationsConst


solvers = [
    GradientSolver(alpha=0.3),
    GradientSplitSolver(alpha=0.3),
    CoordsSolver(alpha=0.3),
    #Evristic(0.3, 0.3),
    ConfigurationsConst(0.5, 1e-4, 0.1),
]

for solver in solvers:
    res = solver(variant2)
    print(res)
