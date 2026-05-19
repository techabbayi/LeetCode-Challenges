1class Solution(object):
2    def search(self, nums, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: int
7        """
8        left = 0
9        right = len(nums) - 1
10
11        while left <= right:
12
13            mid = (left + right) // 2
14
15            if nums[mid] == target:
16                return mid
17
18            # left half sorted
19            if nums[left] <= nums[mid]:
20
21                if nums[left] <= target < nums[mid]:
22                    right = mid - 1
23                else:
24                    left = mid + 1
25
26            # right half sorted
27            else:
28
29                if nums[mid] < target <= nums[right]:
30                    left = mid + 1
31                else:
32                    right = mid - 1
33
34        return -1        