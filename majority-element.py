# https://leetcode.com/problems/majority-element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict_count = {}
        num = 0
        for each in nums:
            if each in dict_count.keys():
                dict_count[each]+=1
                if dict_count[each]> len(nums)/2:
                    num = each
                    break

            else:
                dict_count[each]=1
                if dict_count[each]> len(nums)/2:
                    num = each
                    break
        return num
