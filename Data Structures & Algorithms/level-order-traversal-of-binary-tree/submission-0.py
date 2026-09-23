# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = [root]
        res = []
        if not root:
            return []
        while q:
            level = []
            for i in range(len(q)):
                node = q.pop(0)
                if not node:
                    continue
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
            if level == []:
                continue
            res.append(level)

        return res
            
