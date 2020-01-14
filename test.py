from fib import Fibonacci
import unittest
print(Fibonacci(10))
class TestStringMethods(unittest.TestCase):
    def test_Fib(self):
        self.assertEqual(Fibonacci(10),34)
    def test_bigNum(self):
        self.assertEqual(Fibonacci(20),4181)
if __name__ == '__main__':
    unittest.main()
