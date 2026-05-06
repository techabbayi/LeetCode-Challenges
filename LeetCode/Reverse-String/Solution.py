1class Solution(object):
2    def reverseString(self, s):
3        """
4        :type s: List[str]
5        :rtype: None Do not return anything, modify s in-place instead.
6        """
7        
8        left = 0
9        right = len(s) - 1
10
11        while left < right:
12
13            s[left], s[right] = s[right], s[left]
14
15            left += 1
16            right -= 1
17
18
19        