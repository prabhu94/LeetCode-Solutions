# https://leetcode.com/problems/number-of-islands/
class Solution:
    def __init__(self):
        self.visited = []
        
    def dfs(self,i,j, grid):
        
        self.visited[i][j]=True
        for x in range(-1, 2):
            for y in range(-1, 2):
                if abs(x+y) == 1:
                    if i+x>=0 and i+x<len(grid) and j+y>=0 and j+y < len(grid[0]) and self.visited[i+x][j+y]==False and grid[i+x][j+y] !='0':
                        self.dfs(i+x,j+y, grid)
                        
                    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        for each_row in grid:
            temp_row = []
            for each_val in each_row:
                temp_row.append(False)
            self.visited.append(temp_row)
        
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.visited[i][j] == False and grid[i][j] != '0':
                    self.dfs(i, j, grid)
                    cnt+=1
        return cnt
                
        
