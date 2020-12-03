class Solution:
    def __init__(self):
        self.maxV = 100001
        self.dfn = [0 for _ in range(self.maxV)]  #点搜索的次序编号（时间戳）
        self.low = [self.maxV for _ in range(self.maxV)]   #每个点在这颗树中的，最小的子树的根
        self.vis = [0 for _ in range(self.maxV)]
        self.edgs = [[] for _ in range(self.maxV)]
        self.ans = []
        self.times = 0
    
    def tarjan(self,curr,parent):
        self.times += 1
        self.low[curr] = self.times
        self.dfn[curr] = self.times
        self.vis[curr] = 1
        
        for e in self.edgs[curr]:
            if e == parent:
                continue
                
            if self.vis[e] == 0:
                self.tarjan(e,curr)
                self.low[curr] = min(self.low[curr],self.low[e])
                if self.low[e] > self.dfn[curr]:
                    self.ans.append([curr,e])
            else:
                self.low[curr] = min(self.low[curr],self.dfn[e])
                
        
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        for conn in connections:
            self.edgs[conn[0]].append(conn[1])
            self.edgs[conn[1]].append(conn[0])  
        
        self.tarjan(0,-1)
        return self.ans