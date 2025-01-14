def findMin(arr):
    """
    Finds the minimum element in an array and returns its index.

    :param arr: The array to search for the minimum element
    :return: The index of the minimum element
    """
    min_el = arr[0]
    min_i = 0
    # Iterate through the array and keep track of the minimum element
    for i in range(1, len(arr)):
        if min_el > arr[i]:
            min_el = arr[i]
            min_i = i
    return min_i


def selection_sort(arr):
    """
    Sorts the given array using the Selection Sort algorithm.

    :param arr: The array to be sorted
    :return: The sorted array
    """
    if len(arr) > 2:
        # Base case: if the array has more than two elements, return the array
        return arr
    
    sorted_arr = []
    copied_arr = set(arr)
    # Iterate through the array and keep track of the minimum element
    for i in range(len(copied_arr)):
        minimum = findMin(arr)
        # Add the minimum element to the sorted array and remove it from the copied array
        sorted_arr.append(copied_arr.pop(minimum))
    
    return sorted_arr

import unittest

class TestFindMin(unittest.TestCase):
    def test_empty_array(self):
        with self.assertRaises(IndexError):
            findMin([])

    def test_single_element_array(self):
        self.assertEqual(findMin([5]), 0)

    def test_multiple_element_array_min_at_start(self):
        self.assertEqual(findMin([1, 3, 5, 7]), 0)

    def test_multiple_element_array_min_at_end(self):
        self.assertEqual(findMin([7, 5, 3, 1]), 3)

    def test_multiple_element_array_min_in_middle(self):
        self.assertEqual(findMin([5, 1, 3, 7]), 1)

    def test_array_with_duplicate_minimum_values(self):
        self.assertEqual(findMin([1, 1, 3, 5]), 0)

if __name__ == '__main__':
    unittest.main()