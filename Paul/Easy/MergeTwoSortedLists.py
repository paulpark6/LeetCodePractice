# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #  create an empty list
        #  list 1 vs list 2
        #  add smaller one shrink that list
        #  repeat until one is empty
        new_list = ListNode()
        ptr = new_list
        while (list1 and list2):
            if list1.val <= list2.val:
                ptr.next = list1
                list1 = list1.next
            else:
                ptr.next = list2
                list2 = list2.next
            ptr = ptr.next
        if list1:
            ptr.next = list1
        else:
            ptr.next = list2
        return new_list.next