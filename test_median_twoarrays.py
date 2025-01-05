import unittest
from median_twoarrays import Solution

class TestMedianOfTwoSortedArrays(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()  # Create an instance of Solution
    
    def test_basic_cases(self):
        # Example 1
        self.assertAlmostEqual(self.solution.findMedianSortedArrays([1, 3], [2]), 2.0)
        # Example 2
        self.assertAlmostEqual(self.solution.findMedianSortedArrays([1, 2], [3, 4]), 2.5)
    
    def test_edge_cases(self):
        # One array is empty
        self.assertAlmostEqual(self.solution.findMedianSortedArrays([], [1, 2, 3]), 2.0)
        self.assertAlmostEqual(self.solution.findMedianSortedArrays([1, 2, 3], []), 2.0)
        
        # All elements in one array are smaller
        self.assertAlmostEqual(self.solution.findMedianSortedArrays([1, 2, 3], [4, 5, 6]), 3.5)
        self.assertAlmostEqual(self.solution.findMedianSortedArrays([4, 5, 6], [1, 2, 3]), 3.5)
        
        # Single element arrays
        self.assertAlmostEqual(self.solution.findMedianSortedArrays([1], [2]), 1.5)
        self.assertAlmostEqual(self.solution.findMedianSortedArrays([3], [1, 2]), 2.0)
    
    def test_odd_length(self):
        self.assertAlmostEqual(self.solution.findMedianSortedArrays([1, 3, 5], [2, 4]), 3.0)
        self.assertAlmostEqual(self.solution.findMedianSortedArrays([1, 2], [3, 4, 5]), 3.0)
    
    def test_even_length(self):
        self.assertAlmostEqual(self.solution.findMedianSortedArrays([1, 2, 3], [4, 5, 6]), 3.5)
        self.assertAlmostEqual(self.solution.findMedianSortedArrays([1, 3, 5, 7], [2, 4, 6, 8]), 4.5)
    
    def test_large_arrays(self):
        # Large arrays with alternating values
        nums1 = list(range(0, 1000, 2))  # Even numbers 0-998
        nums2 = list(range(1, 1001, 2))  # Odd numbers 1-999
        self.assertAlmostEqual(self.solution.findMedianSortedArrays(nums1, nums2), 499.5)
        
        # Large arrays with one much smaller than the other
        nums1 = [1, 3, 5]
        nums2 = list(range(100, 200))
        self.assertAlmostEqual(self.solution.findMedianSortedArrays(nums1, nums2), 148.0)

if __name__ == '__main__':
    unittest.main()