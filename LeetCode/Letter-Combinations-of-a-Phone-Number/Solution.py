1class Solution(object):
2    def letterCombinations(self, digits):
3        """
4        :type digits: str
5        :rtype: List[str]
6        """
7
8        if not digits:
9            return []
10
11        phone = {
12            "2": "abc",
13            "3": "def",
14            "4": "ghi",
15            "5": "jkl",
16            "6": "mno",
17            "7": "pqrs",
18            "8": "tuv",
19            "9": "wxyz"
20        }
21
22        result = [""]
23
24        for digit in digits:
25
26            temp = []
27
28            for word in result:
29                for ch in phone[digit]:
30                    temp.append(word + ch)
31
32            result = temp
33
34        return result