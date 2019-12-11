# https://leetcode.com/problems/contains-duplicate
from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums)>0:
            dict_count = Counter(nums)
            if dict_count.most_common()[0][1] ==1:
                return False
            return True
        return False
