# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start, prev = head, None
        while(start):
            nxt = start.next
            start.next = prev
            prev = start
            start = nxt
        return prev