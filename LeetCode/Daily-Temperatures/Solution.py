1class Solution(object):
2    def dailyTemperatures(self, temperatures):
3
4        result = [0] * len(temperatures)
5
6        stack = []
7
8        for i in range(len(temperatures)):
9
10            while stack and temperatures[i] > temperatures[stack[-1]]:
11
12                prev = stack.pop()
13
14                result[prev] = i - prev
15
16            stack.append(i)
17
18        return result