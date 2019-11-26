# https://leetcode.com/problems/basic-calculator-ii/
class Solution:
    def calculate(self, s: str) -> int:

        if len(s) <1:
            return None
        stack = []
        i=0
        while i < len(s):
            if s[i] !=' ':
                if s[i].isdigit() or s[i]=='-':
                    temp = 1
                    if s[i]== '-':
                        print("minus")
                        temp = -1
                        stack.append("+")
                        i+=1
                    n = int(s[i])
                    while i+1<len(s) and s[i+1].isdigit():
                        n = n*10 + int(s[i+1])
                        i+=1
                    print(temp, n, temp*n)
                    stack.append(temp*n)
                    i+=1
                else:
                    stack.append(s[i])
                    i+=1
            else:
                i+=1
        print(stack)
        # first pass
        i=0
        while i < len(stack):
            if stack[i] == '/':
                print(stack[i-1],"/",stack[i+1])
                temp = stack[i-1]/stack[i+1]
                temp_stack = stack[:i-1]
                temp_stack.append(temp)
                temp_stack.extend(stack[i+2:])
                stack = temp_stack.copy()
                print(stack)
            i+=1

        # second pass
        i=0
        while i < len(stack):
            if stack[i] == '*':
                print(stack[i-1],"*",stack[i+1])
                temp = stack[i-1]*stack[i+1]
                temp_stack = stack[:i-1]
                temp_stack.append(temp)
                temp_stack.extend(stack[i+2:])
                stack = temp_stack.copy()
                i=0
                print(stack)
            i+=1
        # third pass
        i=0
        while i < len(stack):
            if stack[i] == '+':
                print(stack[i-1],"+",stack[i+1],"=", stack[i-1]+stack[i+1])
                temp = stack[i-1]+stack[i+1]
                temp_stack = stack[:i-1]
                temp_stack.append(temp)
                temp_stack.extend(stack[i+2:])
                stack = temp_stack.copy()
                i=0
                print(stack)
            i+=1

        # fourth pass
        i=0
        while i < len(stack):
            if stack[i] == '-':
                print(stack[i-1],"-",stack[i+1])
                temp = stack[i-1]-stack[i+1]
                temp_stack = stack[:i-1]
                temp_stack.append(temp)
                temp_stack.extend(stack[i+2:])
                stack = temp_stack.copy()
                print(stack)
                i=0
            i+=1
                
        return round(int(stack[0]))
