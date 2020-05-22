import numpy as np

# this will be the evaluation function that is called each time
from pymop.factory import get_problem

from pymop.problem import Problem

def my_evaluate_func(x, out, *args, **kwargs):  
 f1 = 31*x[:,0] + 38*x[:,1] + 19*x[:,2] + 37*x[:,3] + 45*x[:,4] + 23*x[:,5] + 23*x[:,6])
 f2 = 27*x[:,0] + 35*x[:,1] + 74*x[:,2] + 62*x[:,3] + 22*x[:,4] + 27*x[:,5] + 33*x[:,6])
 f3 = 61*x[:,0] + 56*x[:,1] + 55*x[:,2] + 84.6*x[:,3] + 65*x[:,4] + 73*x[:,5] + 62*x[:,6]
 g1 = x[:,0] + x[:,1] + x[:,2] + x[:,3] + x[:,4] + x[:,5] + x[:,6] - 1
 g2 = 1 - x[:,0] - x[:,1] - x[:,2] - x[:,3] - x[:,4] - x[:,5] - x[:,6]
 out["F"] = anp.column_stack([f1])
 out["G"] = anp.column_stack([g1, g2])
 mask = ["int", "int", "int", "int", "int", "int", "int"]

problem = get_problem(my_evaluate_func, np.array([0, 0 , 0, 0, 0, 0, 0, 0]), np.array([1, 1, 1, 1, 1, 1, 1]))
F, CV = problem.evaluate(np.random.rand(100, 7))



