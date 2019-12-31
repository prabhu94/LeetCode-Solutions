#https://leetcode.com/problems/roman-to-integer
class Solution:
    def romanToInt(self,s):
        stack = []
        i=0
        while i < len(s):
            if s[i]=='I':
                temp = []
                temp.append(s[i])
                if i+1 <len(s):
                    if s[i+1] == 'V' or s[i+1]=='X':
                        temp.append(s[i+1])
                stack.append("".join(temp))
                i+=len(temp)
            elif s[i] =='X':
                temp = []
                temp.append(s[i])
                if i+1 <len(s):
                    if s[i+1] == 'C' or s[i+1]=='L':
                        temp.append(s[i+1])
                stack.append("".join(temp))
                i+=len(temp)
            elif s[i] =='C':
                temp = []
                temp.append(s[i])
                if i+1 <len(s):
                    if s[i+1] == 'D' or s[i+1]=='M':
                        temp.append(s[i+1])
                stack.append("".join(temp))
                i+=len(temp)
            else:
                stack.append(s[i])
                i+=1
        sum_val = 0
        for each in stack:
            if each=='I':
                sum_val+=1
            elif each == 'V':
                sum_val+=5
            elif each == 'IV':
                sum_val+=4
            elif each == 'X': 
                sum_val+=10
            elif each == 'IX': 
                sum_val+=9
            elif each == 'L':
                sum_val+=50
            elif each == 'C':
                sum_val+=100
            elif each == 'D':
                sum_val+=500
            elif each == 'M':
                sum_val+=1000
            elif each == 'XC':
                sum_val+=90
            elif each == 'XL':
                sum_val+=40
            elif each == 'CD':
                sum_val+=400
            elif each == 'CM':
                sum_val+=900
        return sum_val
