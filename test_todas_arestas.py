import unittest
import main

class TestStringMethods(unittest.TestCase):

    def test_APROVADO(self):
        main.q_academico('12 9 8 10')

    def test_REPROVADO(self):
        main.q_academico('12 1 2 3')

if __name__ == '__main__':
    unittest.main()