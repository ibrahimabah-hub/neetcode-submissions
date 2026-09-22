# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def sameKids(p, q):
            if not p and not q:
                return True
            l = True
            if p.left and q.left:
                if (p.left.val == q.left.val):
                    l = sameKids(p.left, q.left)
                else:
                    return False
            elif p.left or q.left:
                return False
            r = True
            if p.right and q.right:
                if p.right.val == q.right.val:
                    r = sameKids(p.right, q.right)
                else:
                    return False
            elif p.right or q.right:
                return False                

            if r and l:
                return True
            else:
                return False
        if not p and not q:
            return True
        elif not p or not q:
            return False

        if p.val == q.val:
            return sameKids(p, q)
        else: 
            return False
