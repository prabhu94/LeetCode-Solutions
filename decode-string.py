# https://leetcode.com/problems/decode-string/
class Solution:
    def decodeString(self, s: str) -> str:
        # s = 3[a2[c]]
        # stack = []
        # iterate over s 
        # if digit or[ or letter push
        #   digit_list
        #   if digit then append to dig list
        #       eval (digit_list)
        # example: 1st pass stack [3,[, ac, 22,[, c 
        # if ] then pop till pop = number
        #   push number*popped to stack
        # 3[a2]2345[c]ef
        # 2 to 5
        # ind = 0
        # ind = 
        
        stack = []
        i = 0
        while i < len(s):
            if s[i] == '[' or s[i].isdigit() or s[i].isalpha():
                
                if s[i].isdigit():
                    n = int(s[i])
                    while i+1<len(s) and s[i+1].isdigit():
                        n = n*10 + int(s[i+1])
                        i+=1
                    stack.append(n)
                elif s[i].isalpha():
                    temp = s[i]
                    while i+1<len(s) and s[i+1].isalpha():
                        temp += s[i+1]
                        i+=1
                    if len(stack)>0 and stack[-1].isalpha():
                        stack[-1] += temp
                    else:
                        stack.append(temp)
                else:
                    stack.append(s[i])
                i+=1
                print(stack)
            else:
                temp = stack.pop()
                stack.pop()
                num = stack.pop()
                temp_string = num*temp
                if len(stack)>0 and stack[-1].isalpha():
                    stack[-1]+=temp_string
                else:
                    stack.append(temp_string)
                i+=1
                print(stack)
        return "".join(stack)
                
