1class Solution(object):
2    def subsets(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: List[List[int]]
6        """
7
8        result = [[]]
9
10        for num in nums:
11
12            temp = []
13
14            for subset in result:
15                temp.append(subset + [num])
16
17            result += temp
18
19        return result        