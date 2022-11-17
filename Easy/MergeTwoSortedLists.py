# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create new list
        list_final = ListNode()
        # pointer for list_final
        list_final_node = list_final
        # pointer for list 1
        list1_node = list1
        # pointer for list 2
        list2_node = list2
        # while loop that ends if both ends
        while ((list1_node.next is not None) or (list2_node.next is not None)):
            # check for smaller item
            if (list1.val < list2.val):
                # add the smaller item to list_final
                list_final_node.val = list1.val
                list_final_node.val = None
                # iterate smaller one
                list1_node = list1.next
            elif (list1.val > list2.val):
                list_final_node.val = list2.val
                list_final_node.val = None
                # iterate smaller one
                list2_node = list1.next                
            elif (list1.val == list2.val): # both have same value
                # add both
                list_final_node.val = list1_node.val
                list_final_node.next = ListNode(list2_node.val, None)                
                list1_node = list1_node.next
                list2_node = list1_node.next
            # show that if one list ended just add the other one at the end
        return list_final