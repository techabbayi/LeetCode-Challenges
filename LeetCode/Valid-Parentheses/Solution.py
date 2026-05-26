1class Solution(object):
2    def isValid(self, n):
3        """
4        :type s: str
5        :rtype: bool
6        """
7        stack = []
8        for char in n:
9            if char == '(':
10                stack.append(')')
11            elif char == '[':
12                stack.append(']')
13            elif char == '{':
14                stack.append('}')
15            else:
16                if not stack or stack.pop() != char:
17                    return False
18        return len(stack) == 0
19
20        