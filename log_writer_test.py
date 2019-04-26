import unittest
from log_writer import LogWriter
import math

class MyTest(unittest.TestCase):

	def setUp(self):
		self.head_text = """
		The following list represents the total number of invisible unicorns in classroom.
		"""
		self.list_data = [1,2,3,4]
		self.test_instance = LogWriter(self.list_data, self.head_text)

	def test_combining_method(self):
		combined_text = self.test_instance.combining_method()
		total_text = "\n\t\tThe following list represents the total number of invisible unicorns in classroom.\n\t\t_________\n After change: \n\n\t\tThe following list ([1, 2, 3, 4]) represents the total number of invisible unicorns in classroom.\n\t\t0 O 0 O 0 O 0 O 0 O 0 O7.483314773547883\nTo seek the holy grail\n2218.473985099097"
		self.assertEqual(total_text, combined_text)
