import unittest

def contar_vocales(mi_string):

    vocales = ('a', 'e', 'i', '0', 'u',)

    resultado = {}

    for letra in mi_string:

        if letra in vocales:

            if letra not in resultado:

                resultado [letra]= 0

            resultado [letra]= 1

    return resultado


class TestContarVocales(unittest.TestCase):

    def test_nada(sefl):

        resultado = contar_vocales('zzz')

        sefl.assertEqual(resultado, {})

    def test_contar_a(self): 

        resultado = contar_vocales('cas')

        self.assertEqual (resultado, {'a': 1})

    def test_contar_aa (self):

        resultado = contar_vocales ('casa')

        self.assertEqual (resultado, {})

    def test_contar_bese (self):

        resultado = contar_vocales ('bese')

        self.assertEqual (resultado, {'e': 2}) 

    def test_contar_besa (self):

        resultado = contar_vocales ('besa')

        self.assertEqual (resultado, {'a': 1, 'e': 1})

    def test_contar_besa (self):

        resultado = contar_vocales ('casanova')

        self.assertEqual (resultado, {'a': 3, 'o': 1})  

    def test_contar_besa (self):

        resultado = contar_vocales ('casanova')

        self.assertEqual (resultado, {'a': 3, 'o': 1})


#unittest.main

while (True):

    palabra = input('ingrese palabra: ')

    print (contar_vocales(palabra))