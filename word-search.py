# https://leetcode.com/problems/word-search
class Solution:
    
    def __init__(self):
        self.visited = []
        self.grid = None
        self.ans = False
        self.word = None
        
        
    def dfs(self,i,j, index):
        if self.grid[i][j] == self.word[index]:
            if index+1==len(self.word):
                self.ans = True
                return self.ans

            # mark the node as visited
            self.visited[i][j] = True
            # search the next node, increment the index if found, and if not a viable option, backtrack
            for x in range(-1,2):
                for y in range(-1,2):
                    if abs(x+y)==1:
                        if i+x>=0 and i+x<len(self.grid) and j+y>=0 and j+y<len(self.grid[0]) and self.visited[i+x][j+y]==False:
                            self.dfs(i+x,j+y, index+1)
                            if self.ans:
                                return True
            self.visited[i][j] = False
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(word)==0:
            return True
        if len(word)>(len(board)*len(board[0])):
            return False
        for each_row in board:
            temp_row = []
            for each_val in each_row:
                temp_row.append(False)
            self.visited.append(temp_row)
        index=0
        self.grid = board
        self.word = word
        # s = []
        
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.ans == False and self.word[0] == board[i][j] and self.visited[i][j] == False:
                    self.dfs(i,j,0)                        
        return self.ans
        
