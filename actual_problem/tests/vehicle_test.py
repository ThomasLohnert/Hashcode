import unittest
from actual_problem.Vehicle import Vehicle
from actual_problem.ride import Ride


class VehicleTest(unittest.TestCase):
    def test_calc_time(self):
        r = Ride(0, (2, 2), (3, 4), 0, 0)
        v = Vehicle(0)

        v.update(r)

        expected = 7
        actual = v.time

        self.assertEqual(expected, actual)

    def test_calc_time_multiple_jobs(self):
        r1 = Ride(0, (2, 2), (3, 4), 0, 0)
        r2 = Ride(0, (5, 4), (0, 0), 0, 0)
        v = Vehicle(0)

        v.update(r1)
        v.update(r2)

        expected = 7 + 11
        actual = v.time

        self.assertEqual(expected, actual)