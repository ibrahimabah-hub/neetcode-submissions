# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(cur):
            if not cur:
                return 0
            if not (cur.left or cur.right):
                return 0
            l = 0
            if cur.left:
                l = 1 + height(cur.left)
            r = 0
            if cur.right:
                r = 1 + height(cur.right)
            #print(f"height at {cur.val} ({l}, {r})")
            return max(l, r)

        if not root:
            return True
        l = height(root.left)
        if not root.left:
            l-=1
        r = height(root.right)
        if not root.right:
            r-=1
        
        if abs(r - l)>1:
            return False
        else:
            return (self.isBalanced(root.left) and self.isBalanced(root.right))