import unittest
from prime_number import nth_prime_number

class PrimeNumberTest(unittest.TestCase):
    def test_nth_prime_number(self):
        self.assertEqual(nth_prime_number(1), 2)
        self.assertEqual(nth_prime_number(2), 3)
        self.assertEqual(nth_prime_number(5), 11)
        self.assertEqual(nth_prime_number(10), 29)
        self.assertEqual(nth_prime_number(20), 71)

if __name__ == '__main__':
    unittest.main()
