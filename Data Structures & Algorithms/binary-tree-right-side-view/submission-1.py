# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = [root]
        res = []
        if not q:
            return
        
        while q:
            level = []
            for i in range(len(q)):
                node = q.pop(0)
                if not node:
                    continue
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
                level.append(node.val)
            if level == []:
                continue
            #print(level)
            res.append(level[0])

        return res
