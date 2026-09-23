# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        def dfs(node, most):
            if not node:
                return 0
            res = 0
            if node.val >= most:
                res = 1
                most = node.val
            if node.left:
                res+= dfs(node.left, most)
            if node.right:
                res+= dfs(node.right, most)
            return res
        
        return dfs(root, root.val)
        

                
