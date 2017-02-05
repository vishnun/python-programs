from unittest import TestCase
from climbing_stairs import *


class TestClimbing_stairs(TestCase):
	def test_climb(self):
		assert climb(2) == 2
		assert climb(1) == 1
		assert climb(0) == 0
		assert climb(6) == 13
		assert climb_i(2) == 2
		assert climb_i(1) == 1
		assert climb_i(0) == 0
		assert climb_i(6) == 13