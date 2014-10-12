import unittest

from demopkg import dummy

class TestDummy(unittest.TestCase):
	def test_no_return_value(self):
		self.assertIs(dummy.useless_function(), None)
