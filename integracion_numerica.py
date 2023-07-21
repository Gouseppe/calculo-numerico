import sympy as sp


def funcion1(x):
    return x * sp.cos(x)

def suma_riemann(funcion,min, max, n):
    h = (max-min)/n
    result = 0
    for i in range(n+1):
        aux = min + (h*i)
        result += h * funcion(aux)
    return result
    

    
def metodo_del_trapecio(funcion,min,max,n):
    h = (max-min)/n
    result = 0
    for i in range(n):
        aux = min + (h*i)
        result += (h * (funcion(aux) + funcion(aux+h)))/2
    return result

# if __name__ == "__main__":
#     print(metodo_del_trapecio(funcion1,0,1, 30))