# -*- coding: utf-8 -*-

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_absolute_truth_and_meaning(self):
        """Sample basic test"""
        assert True


if __name__ == "__main__":
    unittest.main()
