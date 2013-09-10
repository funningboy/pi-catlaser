import unittest
from model import LaserModel

class LaserModelTests(unittest.TestCase):
	def setUp(self):
		self.servos = TestServos()
		self.model = LaserModel(self.servos)

	def test_setxaxis_getxaxis(self):
		self.model.setXAxis(200)
		assert self.model.getXAxis() == 200
		assert self.servos.xaxis == 200

	def test_setyaxis_getyaxis(self):
		self.model.setYAxis(200)
		assert self.model.getYAxis() == 200
		assert self.servos.yaxis == 200

	def test_setxaxis_out_of_bounds_raises_valueerror(self):
		self.assertRaises(ValueError, self.model.setXAxis, 10)
		self.assertRaises(ValueError, self.model.setXAxis, 700)

	def test_setyaxis_out_of_bounds_raises_valueerror(self):
		self.assertRaises(ValueError, self.model.setYAxis, 10)
		self.assertRaises(ValueError, self.model.setYAxis, 700)

	def test_axis_defaults_to_400(self):
		assert self.model.getXAxis() == 400
		assert self.model.getYAxis() == 400
		assert self.servos.xaxis == 400
		assert self.servos.yaxis == 400


class TestServos(object):
	def __init__(self):
		self.xaxis = 0
		self.yaxis = 0

	def setXAxis(self, value):
		self.xaxis = value

	def setYAxis(self, value):
		self.yaxis = value


if __name__ == '__main__':
	unittest.main()