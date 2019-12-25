# https://leetcode.com/problems/shuffle-an-array/submissions/
import random
from itertools import permutations
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = nums[:]
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.original
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        random.shuffle(self.nums)
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
