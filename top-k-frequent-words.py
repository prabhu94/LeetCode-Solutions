#https://leetcode.com/problems/top-k-frequent-words
import heapq
from collections import defaultdict,Counter, OrderedDict

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq_dict = Counter()
        for each in words:
            if each in freq_dict.keys():
                freq_dict[each] +=1
            else:
                freq_dict[each] =1
                
        heap = heapq.nlargest(k, freq_dict.values())
        
        reversed_dict = defaultdict(list)
        
        for key,v in freq_dict.items():
            reversed_dict[v].append(key)
            
        
        extended = []
        prev = -1
        for each in heap:
            if each != prev:
                extended.extend(sorted(reversed_dict[each]))
                prev = each
        return(extended[:k])
