
# https://leetcode.com/problems/longest-substring-without-repeating-characters
class Solution:
    def reset(self, visited):
        for each in visited.keys():
            visited[each] = False
        return visited
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        index = 0
        sums = []
        count = 0
        visited = {}
        
        # define the visited dict
        for each in set(s):
            visited[each] = False
        
        # logic
        if len(s)>0:
            while i<len(s):
                # if not visited increment count
                if visited[s[i]] == False:
                    visited[s[i]] = True
                    count+=1
                    sums.append(count)
                    i+=1
                # if visited then add count 
                else:
                    count=0
                    visited = self.reset(visited)
                    index+=1
                    i = index
            return max(sums)
        else:
            return 0
        
        
