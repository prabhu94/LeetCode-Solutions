#https://leetcode.com/problems/container-with-most-water
import heapq
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # n_largest = heapq.nlargest(3,height)
        
        #  brute force
#         max_area = 0
#         areas = set()
#         for i in range(0,len(height)):
#             for j in range(i, len(height)):
#                 length = j-i
#                 ht = min(height[i], height[j])
#                 area = length*ht
#                 areas.add(area)
        
#         return max(areas)
        
        # O(n)
        l = 0 
        areas = []
        r = len(height)-1
        while l<r:
            if height[l]>height[r]:
                areas.append(height[r]*(r-l))
                r-=1
            else:
                areas.append(height[l]*(r-l))
                l+=1
        print(areas)
        return max(areas)
