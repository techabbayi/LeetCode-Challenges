1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def reverseList(self, head):
8        """
9        :type head: Optional[ListNode]
10        :rtype: Optional[ListNode]
11        """
12        prev = None
13        curr = head
14
15        while curr:
16            next_temp = curr.next
17            curr.next = prev
18            prev = curr
19            curr = next_temp
20        return prev