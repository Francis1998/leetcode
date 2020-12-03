class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        right,left = 0,0
        need,window = {},{}
        for c in t:
            if c not in need:
                need[c] = 0
            need[c]+=1
        valid = 0
        start = 0
        lens = 99999
        while right < len(s):
            c = s[right]
            right+=1
            if c in need:
                if c not in window:
                    window[c]=0
                window[c]+=1
                if window[c] == need[c]:
                    valid+=1
            while valid == len(need):
                if right - left <lens:
                    start = left
                    lens = right - left
                d = s[left]
                left +=1
                if d in need:
                    if window[d] == need[d]:
                        valid-=1
                    window[d] -=1
        print(start,lens)
        return s[start:start+lens]
dp = Solution()
print(dp.minWindow("a","aa"))
