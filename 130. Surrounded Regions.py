class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.

        """
       
        stack = []
        result=[]
        for i in range(len(board[0])):
        
            if board[0][i] == "O":
                stack.append((0, i))
            if board[-1][i] == "O":
                stack.append((len(board)-1, i))
        i=0
        for i in range(len(board)):
            if board[i][0] == "O":
                stack.append((i, 0))
            if board[i][len(board[0])-1] == "O":
                stack.append((i, len(board[0])-1))
        
       
        while stack:
            curr=stack.pop()
            board[curr[0]][curr[1]]="S"
            for move in  [(0,1),(0,-1),(1,0),(-1,0)]:
                x,y=curr[0]+move[0],curr[1]+move[1]
                if x>=0 and y>=0 and x<len(board) and y<len(board[0]) :
                    if  board[x][y]=="O":
                        stack.append((x,y))
                        board[x][y]="S"
       
     
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=="O":
                    board[i][j]="X"
                if board[i][j]=="S":
                    board[i][j]="O"