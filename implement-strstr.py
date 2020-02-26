# https://leetcode.com/problems/implement-strstr
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0:
            return 0
        for i in range(0, len(haystack)):
            if needle in haystack[i:i+len(needle)]:
                return i    
        return -1
                    
