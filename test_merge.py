from unittest import TestCase
from typing import Generator
from merge import merge


class TestMerge(TestCase):

    test_list1 = [1, 6, 10, 11]
    test_list2 = [1, 5, 9]
    expected_list = [1, 1, 5, 6, 9, 10, 11]
    not_iter = None
    diff_range1 = 3
    diff_range2 = 5
    set_to_test = {1, 5, 9}
    dict_to_test = {1: 6, 5: 10}

    def test_check_merge_accepts_iterators(self):
        self.assertEqual((list(merge(self.test_list1, self.test_list2))), self.expected_list,
                         f"Merge did not accepted Iterators.")

    def test_check_merge_returns_generator(self):
        self.assertIsInstance(merge(self.test_list1), Generator, "Returned object is not a generator")

    def test_check_func_accepts_generators(self):
        gen_for_test = (arg for arg in self.test_list1)
        self.assertTrue(merge(gen_for_test), "Generator was not accepted as argument")

    def test_merge_result_sorted(self):
        self.assertEqual(list(merge(self.test_list1, self.test_list2)),
                         sorted(self.test_list1+self.test_list2),
                         f"Merge result was not sorted")

    def test_merge_accepts_iterators_of_diff_len(self):
        self.assertEqual(len(list(merge(range(self.diff_range1), range(self.diff_range2)))),
                         len(range(self.diff_range1)) + len(range(self.diff_range2)),
                         f"Iterators with different length were not correctly processed")

    def test_merge_no_arguments(self):
        with self.assertRaises(Exception, msg='Arguments were passed to function merge()'):
            list(merge())

    def test_merge_accept_only_iter(self):
        with self.assertRaises(Exception, msg='Iter was passed to merge()'):
            list(merge(self.not_iter))

    def test_merge_not_accept_set(self):
        with self.assertRaises(Exception, msg='Set was accepted by merge()'):
            list(merge(self.set_to_test))

    def test_merge_not_accept_dict(self):
        with self.assertRaises(Exception, msg='Dictionary was accepted by merge()'):
            list(merge(self.dict_to_test))
