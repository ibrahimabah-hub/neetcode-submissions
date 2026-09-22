# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(a, b):
            if (not a and not b):
                return True
            elif not a or not b:
                return False
            if a.val != b.val:
                return False

            if not a.left and not b.left:
                l = True
            else:
                l = isSame(a.left, b.left)

            if not a.right and not b.right:
                r = True
            else:
                r = isSame(a.right, b.right)

            return l and r
            

        def findRoot(root, subRoot):
            if not root:
                return root
            if root.val == subRoot.val and isSame(root, subRoot):
                return root

            if root.left:
                if isSame(root.left, subRoot):
                    return root.left
                else:
                    l = findRoot(root.left, subRoot)
            else:
                l = None

            if root.right:
                if isSame(root.right, subRoot):
                    return root.right
                else:
                    r = findRoot(root.right, subRoot)
            else:
                r = None

            return l or r

        if findRoot(root, subRoot):
            return True
        else:
            return False

            