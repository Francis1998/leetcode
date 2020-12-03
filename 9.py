class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1)>len(s2):
            return False
        need = {}
        windows = {}
        for s in s1:
            need[s] = need.get(s,0)+1
        left, right = 0, 0 
        valid = 0
        start = 0
        lens = 99999
        while right<len(s2):
            c = s2[right]
            right+=1
            if c in need:
                windows[c] = windows.get(c,0)+1
                if windows[c] == need[c]:
                    valid +=1
            while valid==len(need):
                if right - left < lens:
                    start = right
                    lens = right - left
                d = s2[left]
                left+=1
                if d in need:
                    if windows[d]==need[d]:
                        valid-=1
                    windows[d] -=1
        if lens == len(s1):
            return True
        return False

dp = Solution()
print(dp.checkInclusion("ab","eibvaoooo"))