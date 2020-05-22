from platypus import NSGAII, Problem, Integer
class Belegundu(Problem):
 def __init__(self):
  super(Belegundu, self).__init__(25, 3, 51)
  self.types[:] = [Integer(0, 1), Integer(0, 1), Integer(0, 1), Integer(0, 1), Integer(0, 1), Integer(0, 1), Integer(0, 1), Integer(0, 1), Integer(0, 1), Integer(0, 1), Integer(0, 1), Integer(0, 1), Integer(0, 1), Integer(0, 1), Integer(0, 1), Integer(0, 1), Integer(0, 1), Integer(0, 1), Integer(0, 1), Integer(0, 1), Integer(0, 1), Integer(0, 1), Integer(0, 1), Integer(0, 1), Integer(0, 1)]
  self.constraints[:] = ["==0", "<=0", "<=0", "<=0", "<=0", "<=0", "<=0", "<=0", "<=0", "<=0", "<=0", "<=0", "<=0", "<=0", "<=0", "<=0", "<=0", "<=0", "<=0", "<=0", "<=0", "<=0", "<=0", "<=0", "<=0", "<=0", ">=0", ">=0", ">=0", ">=0", ">=0", ">=0", ">=0", ">=0", ">=0", ">=0", ">=0", ">=0", ">=0", ">=0", ">=0", ">=0", ">=0", ">=0", ">=0", ">=0", ">=0", ">=0", ">=0", ">=0", ">=0"]
 def evaluate(self, solution):
  x1 = solution.variables[0]
  x2 = solution.variables[1]
  x3 = solution.variables[2]
  x4 = solution.variables[3]
  x5 = solution.variables[4]
  x6 = solution.variables[5]
  x7 = solution.variables[6]
  x8 = solution.variables[7]
  x9 = solution.variables[8]
  x10 = solution.variables[9]
  x11 = solution.variables[10]
  x12 = solution.variables[11]
  x13 = solution.variables[12]
  x14 = solution.variables[13]
  x15 = solution.variables[14]
  x16 = solution.variables[15]
  x17 = solution.variables[16]
  x18 = solution.variables[17]
  x19 = solution.variables[18]
  x20 = solution.variables[19]
  x21 = solution.variables[20]
  x22 = solution.variables[21]
  x23 = solution.variables[22]
  x24 = solution.variables[23]
  x25 = solution.variables[24]
  solution.objectives[:] = [31*x1 + 38*x2 + 19*x3 + 28*x4 + 45*x5 + 23*x6 + 23*x7 + 28*x8 + 37*x9 + 42*x10 + 20*x11 + 25*x12 + 39*x13 + 33*x14 + 37*x15 + 25*x16 + 28*x17 + 23*x18 + 38*x19 + 30*x20 + 21*x21 + 40*x22 + 34*x23 + 41*x24 + 31*x25, 27*x1 + 35*x2 + 62*x3 + 48*x4 + 22*x5 + 27*x6 + 33*x7 + 27*x8 + 48*x9 + 35*x10 + 48*x11 + 33*x12 + 33*x13 + 48*x14 + 27*x15 + 62*x16 + 35*x17 + 48*x18 + 22*x19 + 33*x20 + 62*x21 + 22*x22 + 48*x23 + 27*x24 + 33*x25, 55*x1 + 56*x2 + 59*x3 + 55*x4 + 65*x5 + 73*x6 + 62*x7 + 60*x8 + 54*x9 + 58*x10 + 63*x11 + 59*x12 + 61*x13 + 59*x14 + 57*x15 + 53*x16 + 59*x17 + 60*x18 + 72*x19 + 54*x20 + 57*x21 + 66*x22 + 59*x23 + 51*x24 + 56*x25]
  solution.constraints[:] = [x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8  + x9 + x10 + x11 + x12 + x13 + x14 + x15 + x16 + x17 + x18  + x19 + x20 + x21 + x22 + x23 + x24 + x25 - 1, x1 - 1, x2 - 1, x3 - 1, x4 - 1, x5 - 1, x6 - 1, x7 - 1, x8 - 1, x9 - 1, x10 - 1, x11 - 1, x12 - 1, x13 - 1, x14 - 1, x15 - 1, x16 - 1, x17 - 1, x18 - 1, x19 - 1, x20 - 1, x21 - 1, x22 - 1, x23 - 1, x24 - 1, x25 - 1, x1 - 0, x2 - 0, x3 - 0, x4 - 0, x5 - 0, x6 - 0, x7 - 0, x8 - 0, x9 - 0, x10 - 0, x11 - 0, x12 - 0, x13 - 0, x14 - 0, x15 - 0, x16 - 0, x17 - 0, x18 - 0, x19 - 0, x20 - 0, x21 - 0, x22 - 0, x23 - 0, x24 - 0, x25 - 0]
