# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create stack add to stack by order
        # create new list add by removing the top element in stack
        stack = list()
        new = ListNode()
        ptr = head
        while ptr:
            stack.append(ptr.val)
            ptr = ptr.next
        ptr = new
        while stack:
            ptr.next = ListNode(stack.pop(), None)
            ptr = ptr.next
        return new.next