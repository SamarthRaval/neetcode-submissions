# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float("-inf")

        def dfs(root):
            if not root:
                return 0

            left_value = dfs(root.left)
            left_value = 0 if left_value < 0 else left_value
            right_value = dfs(root.right)
            right_value = 0 if right_value < 0 else right_value

            self.maxSum = max(self.maxSum, root.val + left_value + right_value)

            return root.val + max(left_value, right_value)

        dfs(root)

        return self.maxSum

