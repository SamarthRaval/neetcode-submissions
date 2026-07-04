# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        count = 0

        deque = collections.deque()
        deque.append(root)

        while deque:
            length = len(deque)

            for i in range(length):
                node = deque.popleft()

                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)

            count += 1
        
        return count