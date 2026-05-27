1class Solution(object):
2    def nextGreaterElement(self, nums1, nums2):
3
4        stack = []
5        mp = {}
6
7        for num in nums2:
8
9            while stack and num > stack[-1]:
10                mp[stack.pop()] = num
11
12            stack.append(num)
13
14        while stack:
15            mp[stack.pop()] = -1
16
17        result = []
18
19        for num in nums1:
20            result.append(mp[num])
21
22        return result