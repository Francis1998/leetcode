class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return []
        res = []
        need, win ={},{}
        start,lens = 0,99999
        left, right = 0,0
        valid = 0
        for p1 in p:
            need[p1] = need.get(p1,0)+1
        while right<len(s):
            c = s[right]
            right+=1
            if c in need:
                win[c] = win.get(c,0)+1
                if  win[c] == need[c]:
                    valid += 1
            while valid== len(need):
                if right - left<=lens:
                    start = left
                    lens = right - left
                d = s[left]
                left+=1
                if d in need:
                    if win[d] == need[d]:
                        valid -= 1
                    win[d] -= 1
            if lens == len(p) and start not in res:
                res.append(start)
        return res
dp = Solution()
print(dp.findAnagrams("cbaebaabcd","abc"))
print([0,1,2,3]+[0]*53)