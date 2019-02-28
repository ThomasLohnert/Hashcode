import unittest
from actual_problem.file_io import _parse_rides
from actual_problem.ride import Ride


class RideSchedulerTest(unittest.TestCase):
    def test_given_1_lines_parse_returns_1_rides(self):
        rides = _parse_rides(["0 1 2 3 4 5"])
        self.assertEqual(len(rides), 1)
        self.assertTrue(isinstance(rides[0], Ride))

    def test_given_10_lines_parse_returns_10_rides(self):
        rides = _parse_rides(["0 1 2 3 4 5"] * 10)
        self.assertEqual(len(rides), 10)
        self.assertTrue(isinstance(rides[0], Ride))

    def test_given_1_lines_parse_sets_start_and_end_to_tuple(self):
        rides = _parse_rides(["0 1 2 3 4 5"])
        self.assertTrue(isinstance(rides[0].start_pos, tuple))
        self.assertTrue(isinstance(rides[0].end_pos, tuple))

    def test_given_10_lines_parse_returns_correct_idx(self):
        rides = _parse_rides(["0 1 2 3 4 5"] * 10)
        expected_idx = 0
        for r in rides:
            self.assertEqual(rides[expected_idx].id, expected_idx)
            expected_idx += 1

    def test_given_ride_returns(self):
        pass