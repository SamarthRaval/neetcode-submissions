# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.values = []
        def dfs(root):
            if not root:
                return

            dfs(root.left)

            self.values.append(root.val)

            dfs(root.right)

        dfs(root)

        return self.values[k-1]