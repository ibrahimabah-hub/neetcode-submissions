# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dfs(node, most, least):
            status = True
            if not node:
                return True
            if node.val >=most or node.val<=least:
                return False
            #print(f"{least}<{node.val}<{most}")
            if node.left:
                status = dfs(node.left, node.val, least)
                if status == False:
                    return False
            if node.right:
                status = dfs(node.right, most, node.val)
                if status == False:
                    return False

            return status

        return dfs(root, float("infinity"), float("-infinity"))