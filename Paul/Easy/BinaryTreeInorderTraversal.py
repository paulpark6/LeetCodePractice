# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = list()
        
        def traverse(r):
            if r is None:
                return
            else:
                traverse(r.left)
                lst.append(r.val)
                traverse(r.right)
        traverse(root)
        return lst