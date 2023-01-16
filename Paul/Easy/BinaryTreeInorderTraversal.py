# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = list()
        def traverse(root):
            if root is None:
                return None
            else:
                traverse(root.left)
                out.append(root.val)
                traverse(root.right)
        traverse(root)
        return out
        