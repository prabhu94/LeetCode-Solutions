# https://leetcode.com/problems/palindrome-number/submissions/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        st = list(str(x))
        st_rever = st[:]
        st_rever.reverse()
        print(st)
        for i in range(len(st)):
            if st[i] != st_rever[i]:
                return False
        return True        
        
