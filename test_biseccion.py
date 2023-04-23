from biseccion import biseccion
import unittest

import math

def funcion1(x):
    return math.atan(x) + x -1

def funcion2(x):
    return math.exp(-x) - math.log(x)

class TestBiseccion(unittest.TestCase):

    def test1_biseccion_resultado(self):
        
        a =0
        b =1
        minError = 0.01
        maxIteracion = 100
        resultado = biseccion(a,b,funcion1, minError, maxIteracion)

        self.assertEqual(resultado,0.51953125)

    def test2_biseccion_resultado(self):
        
        a =1
        b =1.5
        minError = 0.01
        maxIteracion = 100
        resultado = biseccion(a,b,funcion2, minError, maxIteracion)
        self.assertEqual(resultado,1.3046875)

    def test3_biseccion_datos_invalidos(self):
        a = 1
        b =1.5
        minError = 0.01
        maxIteracion = 100

        with self.assertRaises(ValueError) as a_exc:
            biseccion('hola',b,funcion2, minError, maxIteracion)

        with self.assertRaises(ValueError) as b_exc:
            biseccion(a,'hola',funcion2, minError, maxIteracion)

        with self.assertRaises(ValueError) as a_mayor_b_exc:
            biseccion(5,1,funcion2, min, maxIteracion)

        with self.assertRaises(ValueError) as min_error_exc:
            # biseccion(a,b,funcion2, 'hola', maxIteracion)
            biseccion(a,b,funcion2, 2, maxIteracion)
            
        with self.assertRaises(ValueError) as max_iteration_exc:
            # biseccion(a,b,funcion2, 0.5, 0)
            # biseccion(a,b,funcion2, 0.5, 201)           
            biseccion(a,b,funcion2, 0.5, 'hola')
        
        with self.assertRaises(TypeError) as f_exc:
            biseccion(a,b,b, 0.01, maxIteracion)
        
        self.assertEqual(str(a_exc.exception), 'a debe ser un tipo real')
        self.assertEqual(str(b_exc.exception), 'b debe ser un tipo real')
        self.assertEqual(str(a_mayor_b_exc.exception), 'a debe ser menor que b (a < b)')
        self.assertEqual(str(min_error_exc.exception), 'minError debe ser un tipo entero entre 0 y 1')
        self.assertEqual(str(max_iteration_exc.exception), 'maxIteracion debe ser tipo entero y no puede superar las 200 iteracoines o ser menor que 1')
        self.assertEqual(str(f_exc.exception), 'f no es una funcion')

