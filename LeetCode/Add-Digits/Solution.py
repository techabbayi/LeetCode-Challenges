1class Solution(object):
2    def addDigits(self, num):
3        """
4        :type num: int
5        :rtype: int
6        """
7        while num >= 10:
8
9            total = 0
10
11            while num > 0:
12                total += num % 10
13                num //= 10
14
15            num = total
16
17        return num