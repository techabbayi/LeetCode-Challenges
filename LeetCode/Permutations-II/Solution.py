1class Solution(object):
2    def permuteUnique(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: List[List[int]]
6        """
7        result = []
8
9        def backtrack(path, remaining):
10
11            # permutation completed
12            if not remaining:
13                result.append(path)
14                return
15
16            used = set()
17
18            for i in range(len(remaining)):
19
20                # skip duplicates
21                if remaining[i] in used:
22                    continue
23
24                used.add(remaining[i])
25
26                backtrack(
27                    path + [remaining[i]],
28                    remaining[:i] + remaining[i+1:]
29                )
30
31        backtrack([], nums)
32
33        return result        