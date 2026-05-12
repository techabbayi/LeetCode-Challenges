1class Solution(object):
2    def combinationSum(self, candidates, target):
3        """
4        :type candidates: List[int]
5        :type target: int
6        :rtype: List[List[int]]
7        """
8        result = []
9
10        def backtrack(start, path, total):
11
12            if total == target:
13                result.append(path)
14                return
15
16            if total > target:
17                return
18
19            for i in range(start, len(candidates)):
20                backtrack(i,
21                          path + [candidates[i]],
22                          total + candidates[i])
23
24        backtrack(0, [], 0)
25
26        return result        