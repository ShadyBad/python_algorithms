def find_min(arr):
    """
    Finds the minimum element in an array and returns its index.

    :param arr: The array to search for the minimum element
    :return: The index of the minimum element
    """
    min_index = 0
    min_value = arr[0]
    for i, el in enumerate(arr[1:]):
        if el < min_value:
            min_index = i + 1
            min_value = el
    return min_index


def selection_sort(arr):
    """
    Sorts the given array using the Selection Sort algorithm.

    :param arr: The array to be sorted
    :return: The sorted array
    """
    if len(arr) < 2:
        # Base case: if the array has more than two elements, return the array
        return arr

    sorted_arr = []
    copied_arr = list(arr)
    # Iterate through the array and keep track of the minimum element
    for _ in range(len(copied_arr)):
        min_index = find_min(copied_arr)
        # Add the minimum element to the sorted array and remove it from the copied array
        sorted_arr.append(copied_arr.pop(min_index))

    return sorted_arr

import unittest

class TestSelectionSort(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(selection_sort([]), [])

    def test_single_element_array(self):
        self.assertEqual(selection_sort([5]), [5])

    def test_already_sorted_array(self):
        self.assertEqual(selection_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        self.assertEqual(selection_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_array_with_duplicate_elements(self):
        self.assertEqual(selection_sort([2, 4, 1, 2, 3]), [1, 2, 2, 3, 4])

    def test_array_with_negative_numbers(self):
        self.assertEqual(selection_sort([-3, 2, -1, 4, 0]), [-3, -1, 0, 2, 4])

    def test_large_array(self):
        import random
        arr = [random.randint(0, 100) for _ in range(100)]
        self.assertEqual(selection_sort(arr), sorted(arr))

if __name__ == '__main__':
    unittest.main()