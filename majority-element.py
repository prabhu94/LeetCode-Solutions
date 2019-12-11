# https://leetcode.com/problems/majority-element

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict_count = Counter(nums)
        if (dict_count.most_common()[0][1])>len(nums)/2:
            return dict_count.most_common()[0][0]
