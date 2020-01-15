from fib import Fibonacci , fib_fast
import unittest
print(Fibonacci(10))
class TestStringMethods(unittest.TestCase):
    def test_Fib(self):
        self.assertEqual(Fibonacci(10),34)
        self.assertEqual(Fibonacci(30),514229)
        self.assertEqual(Fibonacci(35),5702887)
    def test_fastFib(self):
        self.assertEqual(fib_fast(20),4181)

if __name__ == '__main__':
    unittest.main()
