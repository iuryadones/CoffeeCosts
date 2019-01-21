from scipy.optimize import linprog
import numpy as np

#O padrão de entrada dos dados deve ser feita para um problema de maximização

c = np.array([-3, -5])
A = np.array([[1,0], [0,1], [3,2]])
b = np.array([4, 6, 18])
res = linprog(c, A, b)
print(res)
print(f'\n DUAL \n')
Ad = -A.transpose()
resd = linprog(b, Ad, c)
print(f' Os multplicadores de lagrange são:')
print(resd)



# ask = input ('The original problem is a maximization?: Y/N')
# if ask == 'Y' or 'y':
#     resd = linprog(b, Ad, c)
#     print(f' Os multplicadores de lagrange são:{resd}')
# else:
#     resd = linprog(b, Ad, -c)
#     print(f' Os multplicadores de lagrange são:{resd}')
