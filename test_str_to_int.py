from unittest import TestCase
from string_to_int import *


class TestStr_to_int(TestCase):
	def test_str_to_int(self):
		assert str_to_int('9') == 9
		assert str_to_int('100000') == 100000
		assert str_to_int('-123') == -123
		assert str_to_int("234x45") == "Not a number"
