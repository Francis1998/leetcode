class Solution:
    def slidingPuzzle(self, board):
        s = ''.join(str(e) for row in board for e in row)
        if s == "123450":
            return 0
        bq, eq, nq, visited, res = {(s, s.index('0'))},{('123450',5)},set(),set(),0   
        moves = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]
        while bq:
            visited |= bq
            res += 1
            for x, idx in bq:
                for nidx in moves[idx]:
                    print(idx)
                    lx = [*x]
                    lx[idx], lx[nidx] = lx[nidx],lx[idx] 
                    nx = ''.join(lx)
                    if (nx,nidx) not in visited:
                        if (nx,nidx) in eq:
                            return res
                        nq.add((nx,nidx))
            bq,nq = nq,set()
            if len(bq) > len(eq):
                bq, eq = eq, bq
        return -1
        
dp = Solution()
print(ord('a')-ord('b'))