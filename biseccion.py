import math

def biseccion(a,b,f,minError,maxIteracion):

    # revisa las excepciones posibles
    if not isinstance(a, (int,float)):
        raise ValueError('a debe ser un tipo real')
    if not isinstance(b, (int,float)):
        raise ValueError('b debe ser un tipo real')
    if (a > b):
        raise ValueError('a debe ser menor que b (a < b)')
    if (not isinstance(minError, (int,float)) or minError < 0 or minError > 1):
        raise ValueError('minError debe ser un tipo entero entre 0 y 1')
    if (not isinstance(maxIteracion, (int,float)) or maxIteracion > 200 or maxIteracion < 1 ):
        raise ValueError('maxIteracion debe ser tipo entero y no puede superar las 200 iteracoines o ser menor que 1')
    if not (callable(f)):
        raise TypeError("f no es una funcion")

    # inicializacion de variables
    i = 0
    mAc = 0
    mAn = 0
    errorRelativo = 1

    # funcionalidad
    while(maxIteracion >= i and errorRelativo >= minError):
        mAc = (a+b)/2
        fa = f(a)
        fm = f(mAc)

        if( fa*fm >= 0 ):
            a = mAc
        else:
            b = mAc
        if(i != 0):
            errorRelativo =  abs((mAc - mAn)/ mAc)

        mAn = mAc
        i += 1
    return mAc if errorRelativo <= minError else None


def funcion2(x):
    return math.sin(x) - math.exp(-x)
def funcion(x):
    return math.exp(x) - (3*(x**2))
