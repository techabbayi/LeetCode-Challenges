1class Solution(object):
2    def fib(self, n):
3        """
4        :type n: int
5        :rtype: int
6        """
7        if n == 0:
8            return 0
9        if n == 1:
10            return 1
11
12        return self.fib(n-1) + self.fib(n-2)