class Solution(object):
    def recoverOrder(self, order, friends):
        ans = []

        for item in order:
            if item in friends:
                ans.append(item)

        return ans