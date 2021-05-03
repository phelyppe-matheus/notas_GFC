import unittest
import main

class TestStringMethods(unittest.TestCase):

    def test_todos_os_valores_codigo_12(self):
        for i in range(11):
            for x in range(11):
                for y in range(11):
                    main.q_academico(f'12 {i} {x} {y}')

if __name__ == '__main__':
    unittest.main()