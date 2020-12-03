class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #find the center, and trace to opposite endings   if 
        self.count = 0
        n = len(s)
        def helper(i,j):
            while i>=0 and j<n and s[i]==s[j]:
                i-=1
                j+=1
                self.count +=1
        for i in range(n):
            helper(i,i)
            helper(i,i+1)
        return self.count
