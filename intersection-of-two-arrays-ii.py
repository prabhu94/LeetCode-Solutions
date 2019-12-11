# https://leetcode.com/problems/intersection-of-two-arrays-ii
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_c = Counter(nums1)
        nums2_c = Counter(nums2)
        inter = set(nums1).intersection(set(nums2))
        temp = []
        for each in inter:
            if nums1_c[each] >= nums2_c[each]:
                for i in range(nums2_c[each]):
                    temp.append(each)
            else:
                for i in range(nums1_c[each]):
                    temp.append(each)
        return temp
            
