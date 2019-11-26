# https://leetcode.com/problems/permutations/
# easy solution using itertools
from itertools import  permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return permutations(nums)

# manual solution
