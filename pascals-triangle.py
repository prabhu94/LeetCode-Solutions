#https://leetcode.com/problems/pascals-triangle
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans_list = []
        if numRows == 1:
            ans_list.append([1])
            return(ans_list)
        if numRows == 2:
            ans_list.append([1])
            ans_list.append([1,1])
            return(ans_list)

        if numRows>2:
            ans_list.append([1])
            ans_list.append([1,1])
        
            for i in range(2, numRows):
                ans_list.append([])
                ans_list[i].append(1)
                for j in range(len(ans_list[i-1])-1):
                    temp = ans_list[i-1][j] + ans_list[i-1][j+1] 
                    ans_list[i].append(temp)
                ans_list[i].append(1)
                
            return(ans_list)        
