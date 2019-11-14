#https://leetcode.com/problems/reverse-integer/submissions/
class Solution:
    def reverse(self, x: int) -> int:
        if x< -2**31 and x> (2**31 -1):
            return 0
        is_neg = False
        if x<0:
            is_neg=True
        
        abs_num = abs(x)
        abs_s = list(str(abs_num))
        abs_s.reverse()
        if -int("".join(abs_s))< -2**31 and int("".join(abs_s))> (2**31 -1):
            return 0

        if is_neg:
            return -int("".join(abs_s))
        return int("".join(abs_s))
        
