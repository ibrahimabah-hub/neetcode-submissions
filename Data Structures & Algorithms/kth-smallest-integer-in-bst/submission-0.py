# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node, least, k):
            if len(least)==k:
                return least
            if node.left:
                least = dfs(node.left, least, k)
            if len(least)<k:
                least.append(node.val)
                if node.right:
                    least = dfs(node.right, least, k)
            return least
            
        ks = dfs(root, [], k)
        #print(ks)
        return ks[-1]
                
            

            



            

