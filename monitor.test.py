import unittest
from monitor import is_inrange, check_vitals, vitals_ok


class MonitorTest(unittest.TestCase):
    def test_vitals_ok(self):
        self.assertTrue(vitals_ok(98.1, 70, 98))
        self.assertFalse(vitals_ok(99, 102, 70))

    def test_is_in_range(self):
        self.assertTrue(is_inrange(96, 95, 102))
        self.assertFalse(is_inrange(110, 95, 102))

    def test_check_vitals(self):
        self.assertTrue(check_vitals(96, 95, 102, "sample error message!"))
        self.assertFalse(check_vitals(110, 95, 102, "sample error message!"))


if __name__ == "__main__":
    unittest.main()
