def binary_search(arr, target):
    """
    Searches for an element in an array using binary search.

    Time complexity: O(log n)
    Space complexity: O(1)

    Args:
        arr: A sorted list of elements to search through.
        target: The element to look for in the array.

    Returns:
        The index of the target element if it is found, None otherwise.
    """
    # Validate input
    if arr is None or not isinstance(arr, list):
        raise ValueError("Input must be a list.")
    
    # Initialize variables
    arr_len = len(arr)
    low, high = 0, arr_len - 1
    
    # Binary search
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        
        if guess == target:
            # If the element is found, ensure we return the first occurrence
            while mid > 0 and arr[mid-1] == target:
                mid -= 1
            return mid
        elif guess > target:
            # If the guess is too high, look at the lower half of the array
            high = mid - 1
        else:
            # If the guess is too low, look at the upper half of the array
            low = mid + 1
    
    # If the element is not found, return None
    return None

import unittest
class TestBinarySearch(unittest.TestCase):
    def test_empty_array(self):
        self.assertIsNone(binary_search([], 5))
    def test_single_element_found(self):
        self.assertEqual(binary_search([5], 5), 0)
    def test_single_element_not_found(self):
        self.assertIsNone(binary_search([5], 3))
    def test_multiple_elements_found(self):
        arr = [1, 3, 5, 7, 9]
        self.assertEqual(binary_search(arr, 5), 2)
    def test_multiple_elements_not_found(self):
        arr = [1, 3, 5, 7, 9]
        self.assertIsNone(binary_search(arr, 6))
    def test_duplicate_elements(self):
        arr = [1, 3, 3, 5, 5, 7]
        self.assertEqual(binary_search(arr, 3), 1)
    def test_edge_cases(self):
        arr = [1, 3, 5, 7, 9]
        self.assertEqual(binary_search(arr, 1), 0)
        self.assertEqual(binary_search(arr, 9), 4)
        self.assertEqual(binary_search(arr, 5), 2)
if __name__ == '__main__':
    unittest.main()