# from scipy.optimize import linprog
# c = [60, 40, 50]
# A = [[20, 10, 10], [10, 10, 20]]
# b = [350, 400]
# res = linprog(c, A, b)
# print(res)

from scipy.optimize import linprog
c = [-3, -5]
A = [[1,0], [0,1],[3,2]]
b = [4, 6, 18]
res = linprog(c, A, b)
print(res)
