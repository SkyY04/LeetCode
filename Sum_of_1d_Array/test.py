import unittest
from Sum_of_1d_Array import Solution

class Lab1TestCase(unittest.TestCase):
    """These are the test cases for functions and classes"""

    def test_runningSum1(self):
        nums=[1,2,3,4]
        solution=Solution()
        self.assertEqual(solution.runningSum(nums), [1,3,6,10])
    
    def test_runningSum1(self):
        nums=[1,1,1,1,1]
        solution=Solution()
        self.assertEqual(solution.runningSum(nums), [1,2,3,4,5])

    def test_runningSum1(self):
        nums=[3,1,2,10,1]
        solution=Solution()
        self.assertEqual(solution.runningSum(nums), [3,4,6,16,17])
        
if __name__ == '__main__':
    unittest.main()