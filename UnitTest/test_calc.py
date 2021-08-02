import unittest
import calc


class TestCalc(unittest.TestCase):
	# run before every single test
	def setUp(self):
		pass

	# run after every single test
	def tearDown(self):
		pass
		
	def test_add(self):
		self.assertEqual(calc.add(10, 5), 15)
		self.assertEqual(calc.add(-1, 1), 0)
		self.assertEqual(calc.add(-1, -1), -2)

	def test_divide(self):
		self.assertEqual(calc.divide(10, 2), 5)

# Without context manager
		self.assertRaises(ValueError, calc.divide, 10, 0)

# With context manager
		with self.assertRaises(ValueError):
			calc.divide(10, 0)


if __name__ == '__main__':
	unittest.main()
