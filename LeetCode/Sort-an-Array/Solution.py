1class Solution(object):
2    def sortArray(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: List[int]
6        """
7        if len(nums) <= 1:
8            return nums
9
10        mid = len(nums) // 2
11        left = self.sortArray(nums[:mid])
12        right = self.sortArray(nums[mid:])
13
14        return self.merge(left, right)
15
16    def merge(self, left, right):
17        result = []
18        i = j = 0
19
20        while i < len(left) and j < len(right):
21            if left[i] < right[j]:
22                result.append(left[i])
23                i += 1
24            else:
25                result.append(right[j])
26                j += 1
27
28        result.extend(left[i:])
29        result.extend(right[j:])
30        return result
31
32        