# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inv(root):
            if not root:
                return
            node = root.left
            root.left = root.right
            root.right = node
            if root.left:
                inv(root.left)
            if root.right:
                inv(root.right)

        inv(root)
        return root

        