# https://leetcode.com/problems/implement-strstr
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0:
            return 0
        
        for i in range(0, len(haystack), len(needle)):
            if needle == haystack[i:i+len(needle)]:
                print("yes", haystack[i:i+len(needle)])
                return i
            else:
                return -1
            
