from platypus import NSGAII, Problem, Integer
class Belegundu(Problem):
 def __init__(self):
  super(Belegundu, self).__init__(7, 3, 15)
  self.types[:] = [Integer(0, 1), Integer(0, 1), Integer(0, 1), Integer(0, 1), Integer(0, 1), Integer(0, 1), Integer(0, 1)]
  self.constraints[:] = ["==0", "<=0", "<=0", "<=0", "<=0", "<=0", "<=0", "<=0", ">=0", ">=0", ">=0", ">=0", ">=0", ">=0", ">=0"]
 def evaluate(self, solution):
  x1 = solution.variables[0]
  x2 = solution.variables[1]
  x3 = solution.variables[2]
  x4 = solution.variables[3]
  x5 = solution.variables[4]
  x6 = solution.variables[5]
  x7 = solution.variables[6]
  solution.objectives[:] = [31*x1 + 38*x2 + 19*x3 + 37*x4 + 45*x5 + 23*x6 + 23*x7, 27*x1 + 35*x2 + 74*x3 + 62*x4 + 22*x5 + 27*x6 + 33*x7, 61*x1 + 56*x2 + 55*x3 + 84.6*x4 + 65*x5 + 73*x6 + 62*x7]
  solution.constraints[:] = [x1 + x2 + x3 + x4 + x5 + x6 + x7 - 1, x1 - 1, x2 - 1, x3 - 1, x4 - 1, x5 -1, x6 - 1, x7 - 1, x1 - 0, x2 - 0, x3 - 0, x4 - 0, x5 - 0, x6 - 0, x7 - 0]