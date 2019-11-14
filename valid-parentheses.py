#https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return True
        mapper = {'(':')','{':'}','[':']'}
        temp_list = []
        for each in s:
            if each in ('({['):
                print("yes")
                temp_list.append(each)
            else:
                print("no")
                if len(temp_list)==0:
                    return False
                else:
                    popped = temp_list.pop()
                    if mapper[popped] == each:
                        continue
                    else:
                        return False
        if len(temp_list)==0:
            return True
        else:
            return False
                    
            
            
