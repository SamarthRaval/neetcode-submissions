# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.value = float("-inf")
        self.flag = True

        def dfs(root):
            if not root:
                return

            dfs(root.left)

            if self.value < root.val:
                self.value = root.val
            else:
                self.flag = False
                return

            dfs(root.right)

            return

        dfs(root)

        return self.flag
            