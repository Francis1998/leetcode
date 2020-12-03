class Solution:
    def __init__(self):
        self.flag =0
    def exist(self, board, word):
        #全排、找结果。0mn 找出头子母的所有位置；可以先找头部在哪，有目的性的去找下一个
        FirstPlace = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    FirstPlace.append([i,j])
        if len(FirstPlace)==0:
            return False
        res = []
        def findstarttwo(x,y,boardfunc,index_word):
            if index_word == len(word):
                self.flag = 1
                return
            
            if x>len(board)-1 or x<0 or y>len(board[0])-1 or y<0:
                return
            print(res,index_word)
            if board[x][y]==word[index_word] and [x,y] not in res:
                res.append([x,y])
                findstarttwo(x+1,y,boardfunc,index_word+1)
                findstarttwo(x-1,y,boardfunc,index_word+1)
                findstarttwo(x,y+1,boardfunc,index_word+1)
                findstarttwo(x,y-1,boardfunc,index_word+1)
                res.remove([x,y])
            if board[x][y]!=word[index_word]:
                return
            return
                
        for i in range(len(FirstPlace)):
            res = []
            findstarttwo(FirstPlace[i][0],FirstPlace[i][1],board,0)
            if self.flag ==1:
                return True
        return False
board = [["A","B","C","E",],["S","F","C","S",],["A","D","E","E",],]
word = "ABCCED"
dp = Solution()

print(dp.exist(board,word))
