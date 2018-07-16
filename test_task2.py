from unittest import TestCase

import task2


class TestTask2(TestCase):

    def setUp(self):
        """Init"""

    def test_task2(self):
        """Test for is task2"""
        self.assertEqual(task2.count([1, 2, 1]), 1)
        self.assertEqual(task2.count([1, 2, 3, 2]), 2)
        self.assertEqual(task2.count([1, 2, 5, 4, 5]), 5)
        self.assertEqual(task2.count([1, 2, 2, 4, 4, 4]), 4)
        self.assertEqual(task2.count([1, 2, 3, 6, 6, 5, 6]), 6)
        self.assertEqual(task2.count([1, 2, 3, 4, 3, 2, 3, 7]), 3)
        self.assertGreater(task2.count([5, 6, 7, 9, 9, 8]), 5)
        self.assertLess(task2.count([2, 1, 4, 2, 5, 1, 2, 5, 7]), 5)

    def tearDown(self):
        """Finish"""
