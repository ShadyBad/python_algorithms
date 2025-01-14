def quicksort(arr: list, low: int = 0, high: int = None) -> list:
    """
    Sorts the given array using the Quick Sort algorithm.

    :param arr: The array to be sorted
    :param low: The starting index of the array, defaults to 0
    :param high: The ending index of the array, defaults to the length of the array
    :return: The sorted array
    """
    # Base case for recursion
    if len(arr) < 2:
        return arr
    
    # Choose a pivot from the array
    pivot = arr[0]

    # Divide the array into two subarrays, one with elements less than the pivot and one with elements greater than the pivot
    less = [i for i in arr[1:] if i <= pivot]
    more = [i for i in arr[1:] if i > pivot]

    # Recursively sort the two subarrays
    return quicksort(less) + [pivot] + quicksort(more)

import unittest

class TestQuicksort(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(quicksort([]), [])

    def test_single_element_array(self):
        self.assertEqual(quicksort([5]), [5])

    def test_already_sorted_array(self):
        self.assertEqual(quicksort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        self.assertEqual(quicksort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_array_with_duplicate_elements(self):
        self.assertEqual(quicksort([2, 4, 1, 2, 3]), [1, 2, 2, 3, 4])

    def test_array_with_negative_numbers(self):
        self.assertEqual(quicksort([-3, 2, -1, 4, 0]), [-3, -1, 0, 2, 4])

    def test_large_array(self):
        import random
        arr = [random.randint(0, 100) for _ in range(100)]
        self.assertEqual(quicksort(arr), sorted(arr))

if __name__ == '__main__':
    unittest.main()