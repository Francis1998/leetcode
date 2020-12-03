"""
Counter('abracadabra').most_common(3)
[('a', 5), ('r', 2), ('b', 2)]
(tong shu - 1)*(n+1) + zuihouyigetongshijian
"""
from collections import Counter
class Solution(object):
    def leastInterval(self,task,n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        
        """
        ct = Counter(task)
        nb = ct.most_common(1)[0][1]
        last = list(ct.values()).count(nb)
        return max((nb-1)*(n+1) + last,len(task))
dp = Solution()
print(dp.leastInterval(["A","A","A","B","B","B"],2))