import unittest
import main

class TestStringMethods(unittest.TestCase):

    def test_maior_que_5(self):
        main.q_academico('12 9 8 10')

    def test_menor_que_5(self):
        main.q_academico('12 1 2 3')

    def test_igual_a_5(self):
        main.q_academico('12 5 5 5')

if __name__ == '__main__':
    unittest.main()