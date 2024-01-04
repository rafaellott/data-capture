import unittest
from data_capture.main import DataCapture


class TestingDataCaptureNumNotExists(unittest.TestCase):

    def setUp(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(3)
        capture.add(5)
        capture.add(8)
        capture.add(8)
        capture.add(9)
        self.stats = capture.build_stats()

    # LOWEST
    def test_num_not_exist_lt_lowest(self):
        """Get the less() on non-existing number below the lowest value."""
        self.assertEqual(0, self.stats.less(2))

    def test_num_not_exist_gt_lowest(self):
        """Get the greater() on non-existing number below the lowest value."""
        self.assertEqual(6, self.stats.greater(2))

    def test_both_num_not_exist_bt_lowest(self):
        """Get the between() on non-existing number below the lowest value."""
        self.assertEqual(0, self.stats.between(1, 2))

    def test_first_num_not_exist_bt_lowest(self):
        """Get the between() on non-existing number below the lowest value."""
        self.assertEqual(2, self.stats.between(1, 3))

    # MIDDLE
    def test_num_not_exist_lt_middle(self):
        """Get the less() on non-existing number in middle of list."""
        self.assertEqual(2, self.stats.less(4))

    def test_num_not_exist_gt_middle(self):
        """Get the greater() on non-existing number in middle of list."""
        self.assertEqual(3, self.stats.greater(6))

    def test_both_num_not_exist_bt_middle_null(self):
        """Get the between() on both non-existing number in middle of list."""
        self.assertEqual(0, self.stats.between(6, 7))

    def test_first_num_not_exist_bt_middle_exists(self):
        """Get the between() on first non-existing number in middle of list."""
        self.assertEqual(3, self.stats.between(7, 9))

    def test_second_num_not_exist_bt_middle_exists(self):
        """Get the between() on first non-existing number in middle of list."""
        self.assertEqual(1, self.stats.between(5, 7))

    # HIGHEST
    def test_num_not_exist_lt_highest(self):
        """Get the less() on non-existing number above the highest value."""
        self.assertEqual(6, self.stats.less(10))

    def test_num_not_exist_gt_highest(self):
        """Get the greater() on non-existing number above the highest value."""
        self.assertEqual(0, self.stats.greater(11))

    def test_both_num_not_exist_bt_highest(self):
        """Get the between() on non-existing number above the highest value."""
        self.assertEqual(0, self.stats.between(10, 12))

    def test_first_num_not_exist_bt_highest(self):
        """Get the between() on non-existing number above the highest value."""
        self.assertEqual(1, self.stats.between(9, 10))


class TestingDataCaptureComplex(unittest.TestCase):
    def setUp(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(3)
        capture.add(4)
        capture.add(5)
        capture.add(6)
        capture.add(5)
        capture.add(9)
        capture.add(7)
        capture.add(10)
        capture.add(9)
        capture.add(12)
        capture.add(9)
        capture.add(12)
        capture.add(15)
        capture.add(18)
        self.stats = capture.build_stats()

    def test_stats_existing_numbers(self):
        # LESS
        self.assertEqual(7, self.stats.less(9))
        self.assertEqual(3, self.stats.less(5))

        # GREATER
        self.assertEqual(9, self.stats.greater(6))
        self.assertEqual(13, self.stats.greater(3))

        # BETWEEN
        self.assertEqual(10, self.stats.between(3, 9))
        self.assertEqual(5, self.stats.between(7, 10))

    def test_stats_non_existing_numbers(self):
        self.assertEqual(7, self.stats.less(9))
        self.assertEqual(0, self.stats.less(2))
        self.assertEqual(7, self.stats.less(8))
        self.assertEqual(15, self.stats.less(20))
        self.assertEqual(4, self.stats.greater(11))
        self.assertEqual(15, self.stats.greater(1))
        self.assertEqual(9, self.stats.greater(6))
        self.assertEqual(15, self.stats.between(2, 20))
        self.assertEqual(4, self.stats.between(8, 10))
        self.assertEqual(6, self.stats.between(8, 13))
        self.assertEqual(0, self.stats.between(19, 55))

    def test_with_basic_operator(self):
        # LESS
        self.assertEqual(7, self.stats < 9)
        self.assertEqual(3, self.stats < 5)

        # GREATER
        self.assertEqual(9, self.stats > 6)
        self.assertEqual(13, self.stats > 3)


if __name__ == '__main__':
    unittest.main()
