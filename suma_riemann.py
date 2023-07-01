import sympy as sp


def funcion1(x):
    return x * sp.cos(x**2)

def integrar(funcion, n, min, max):
    h = (max-min)/n
    result = 0
    for i in range(n+1):
        aux = min + (h*i)
        result += h * funcion(aux)
    return result
    

print(integrar(funcion1,5,0,1))

