# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {val:i for i, val in enumerate(inorder)}
        length = len(preorder)
        self.pre_idx = 0

        def dfs(left, right):
            if left > right:
                return None

            root = TreeNode(preorder[self.pre_idx])
            self.pre_idx += 1

            midpoint = inorder_index[root.val]

            root.left = dfs(left, midpoint-1)
            root.right = dfs(midpoint+1, right)

            return root

        return dfs(0, length-1)