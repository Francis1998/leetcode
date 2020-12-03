class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        dp[i][j] judge s[i][j] palindromic 
        if i==j count+=1 
        if s[i] == s[j] i-j = 1 
        if s[i] == s[j] dp[i+1][j-1] dp[i][j] is palindromic

        """
        #find the center, and trace to opposite endings   if 
        count = 0
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i+1):
                if s[i]==s[j] and (i - j <2 or dp[j + 1][i - 1]):
                    dp[j][i] = 1
                    count +=1
        return count
