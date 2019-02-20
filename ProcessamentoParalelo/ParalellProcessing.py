# from multiprocessing import Pool
# def f(x):
#     return x*x
# if __name__ == "__main__":
#     with Pool(5) as p:
#         r = p.map(f,range(10))
#     print(r)


#################################################


# from multiprocessing import Pool
# def f(x):
#     return x*x
# if __name__ == "__main__":
#     with Pool(5) as p:
#         r = p.map(f,range(10000))
#     print(r)


##########################################################3333

#################################################


# from multiprocessing import Pool
# def f(x):
#     return x*x
# if __name__ == "__main__":
#     with Pool(4) as p:
#         r = p.map(f,range(10000))
#     print(r)



#################################################################

# from math import e # -*- coding: utf-8 -*-
#
# from multiprocessing import Pool
# def f(x):
#     return x*x
# def g(x):
#     return e**x
# if __name__ == "__main__":
#     with Pool(20) as p:
#         r = p.map(f,range(10000))
#     print(r)
#
# if __name__ == "__main__":
#     with Pool(20) as p:
#         r = p.map(g,range(10))
#     print(r)

####################################################

from math import e # -*- coding: utf-8 -*-

from multiprocessing import Pool
def f(x):
    return x*x
def g(x):
    return e**x
if __name__ == "__main__":
    with Pool(3) as p:
        r = p.map(f,range(10000))
    print(r)


    with Pool(3) as p:
        r = p.map(g,range(100))
    print(r)
