# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        cur = TreeNode()
        cur.left = root
        def isLeaf(node):
            if node and (node.left or node.right):
                return False
            return True

        def dfs(node):
            if isLeaf(node):
                return
            if node.left:
                dfs(node.left)
                print(f'checked {node.val}s left')
                if isLeaf(node.left) and node.left.val==target:
                    node.left=None
                    print('chopped')
            if node.right:
                dfs(node.right)
                print(f'checked {node.val}s right')
                if isLeaf(node.right) and node.right.val==target:
                    node.right=None
                    print('chopped')


        dfs(cur)
        return cur.left
