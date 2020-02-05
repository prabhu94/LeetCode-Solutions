#https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr = float('inf')
        curr_pointer = 0
        for i in range(len(nums)):
            if curr != nums[i]:
                nums[curr_pointer] = nums[i]
                curr_pointer +=1
                curr = nums[i]
        return curr_pointer
                
