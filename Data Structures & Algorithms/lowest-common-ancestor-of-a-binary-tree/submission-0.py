# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pd = set()
        qd = set()
        lowk = []
        def descend(root, statq, statp):
            if not root:
                return statq, statp

            if root==p:
                pd.add(root)
                statq = True

            if root==q:
                qd.add(root)
                statp = True

            if root.right and (not statp or not statq):
                rq, rp = descend(root.right, False, False)
                statp = statp or rp
                statq = statq or rq

            if root.left and (not statp or not statq):
                lq, lp = descend(root.left, False, False)
                statp = statp or lp
                statq = statq or lq

            if len(lowk)<1 and statp and statq:
                lowk.append(root)

            return statq, statp

        descend(root, False, False)
        return lowk[0]
            