# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(r):
            if r is None:
                return None
            traverse(r.left)
            traverse(r.right)
            tmp = r.left
            r.left = r.right
            r.right = tmp
        traverse(root)
        return root
        