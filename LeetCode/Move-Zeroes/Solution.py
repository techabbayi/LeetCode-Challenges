1class Solution(object):
2    def moveZeroes(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: None Do not return anything, modify nums in-place instead.
6        """
7        j = 0
8        for i in range(len(nums)):
9            if nums[i] != 0:
10                nums[i], nums[j] = nums[j], nums[i]
11                j += 1