1class Solution(object):
2    def climbStairs(self, n):
3        """
4        :type n: int
5        :rtype: int
6        """
7                # base cases
8        if n == 1:
9            return 1
10
11        if n == 2:
12            return 2
13
14        # fibonacci style
15        a = 1
16        b = 2
17
18        for i in range(3, n + 1):
19            c = a + b
20            a = b
21            b = c
22
23        return b