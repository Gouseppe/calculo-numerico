import sympy as sp


# def funcion1(x):
#     return x * sp.cos(x**2)

def integrar(funcion,min, max, n):
    h = (max-min)/n
    result = 0
    for i in range(n+1):
        aux = min + (h*i)
        result += h * funcion(aux)
    return result
    
# if __name__ == "__main__":
#     print(integrar(funcion1,0,1, 20000))
    
