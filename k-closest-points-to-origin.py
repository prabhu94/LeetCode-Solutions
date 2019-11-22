# https://leetcode.com/problems/k-closest-points-to-origin/
import math, heapq
from collections import defaultdict
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distances = defaultdict(list)
        for each in points:
            dist = ((each[0])**2+(each[1])**2)**(1/2)
            distances[dist].append(each)
        
        heap = heapq.nsmallest(K, distances.keys())
        extended = []
        prev = -1
        for each in heap:
            if each != prev:
                extended.extend(distances[each])
                prev = each
        return(extended[:K])
