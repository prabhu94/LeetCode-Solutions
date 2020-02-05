# https://leetcode.com/problems/remove-element/
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        curr_pointer = 0
        for i in range(len(nums)):
            if val != nums[i]:
                nums[curr_pointer] = nums[i]
                curr_pointer +=1
        return curr_pointer
