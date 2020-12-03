class Solution:
    def primePalindrome(self, N: int) -> int:
        if N <= 2:
            return 2

        def is_prime(n):
            for i in range(2, math.floor(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True

        while True:
            if N % 2 == 0:
                N += 1
                continue
            s = str(N)
            if len(s) == 8:
                N = 10 ** 8
                continue
            if s == s[::-1] and is_prime(N):
                return N
            N += 2
        return 0

class Solution(object):
    def primePalindrome(self, N):
        def is_prime(n):
            return n > 1 and all(n % d for d in xrange(2, int(n**.5) + 1))

        def reverse(x):
            ans = 0
            while x:
                ans = 10 * ans + x % 10
                x /= 10
            return ans

        while True:
            if N == reverse(N) and is_prime(N):
                return N
            N += 1
            if 10**7 < N < 10**8:
                N = 10**8