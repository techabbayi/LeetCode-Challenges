1class Solution(object):
2    def partitionLabels(self, s):
3        """
4        :type s: str
5        :rtype: List[int]
6        """
7
8        last = {}
9
10        # store last index
11        for i in range(len(s)):
12            last[s[i]] = i
13
14        result = []
15
16        start = 0
17        end = 0
18
19        for i in range(len(s)):
20
21            end = max(end, last[s[i]])
22
23            # partition found
24            if i == end:
25                result.append(end - start + 1)
26                start = i + 1
27
28        return result