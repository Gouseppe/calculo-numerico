import sympy as sp

    
def euler(funcion, t_min, t_max, y_min, n):
    h = (t_max - t_min)/n
    t_actual = 0   
    y_actual = y_min
    y_siguiente = 0
    diccionario = {}

    for i in range(n+1):
        t_actual = t_min + (h*i)
        y_siguiente = y_actual + (h*funcion(t_actual,y_actual)) 
        diccionario[i] = y_actual
        y_actual = y_siguiente

    return diccionario
        


# if __name__ == '__main__' :
#     print(euler( lambda t, y: 1 + (t-y)**2, 2, 3, 1, 4))
    