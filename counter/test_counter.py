"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""

import unittest
from counter import Counter


class TestCounterSingleton(unittest.TestCase):
    def test_singleton_of_the_instance(self):
        """Checks that two instances of Counter are the same object."""
        c1 = Counter()
        c2 = Counter()
        self.assertIs(c1, c2)

    def test_shared_count_in_all_instances(self):
        """Checks that the count is shared between instances."""
        c1 = Counter()
        c2 = Counter()
        c1.increment()
        self.assertEqual(c1.count, c2.count)

    def test_count_not_reset_to_zero(self):
        """Checks that the count is not reset to 0 when a new instance is created after incrementing the count."""
        c1 = Counter()
        c1.increment()
        count_before_reset = c1.count
        c2 = Counter()
        self.assertEqual(count_before_reset, c2.count)
