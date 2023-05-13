import sympy as sp


def algoritmoNR(expr, valor, simbolo, minError, maxRepeticiones):
    def funcionSucesiva(expr, fDerivada, simbolo, xi):
        return xi - (expr.subs(simbolo, xi) / fDerivada.subs(simbolo, xi))

    xAnterior = 0
    xActual = valor
    fD = expr.diff(simbolo)
    error = 1
    repeticiones = 0

    while (error >= minError and repeticiones < maxRepeticiones):
        xAnterior = xActual
        xActual = funcionSucesiva(expr, fD, simbolo, xActual)

        error = abs((xActual - xAnterior) / xActual)
        repeticiones += 1

    print('El error es: ', error, '\nNumero de repeticiones: ', repeticiones, '\nxActual es: ', xActual)
    return error


if __name__ == '__main__':
    x = sp.Symbol('x')
    expr = (x-2)**2 - sp.ln(x)
    print(expr)
    exprDerivada = expr.diff(x)
    print(exprDerivada)
