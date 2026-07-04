# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        deque = collections.deque()

        deque.append(root)

        output = []

        while deque:
            length = len(deque)
            inner = []
            for i in range(length):
                node = deque.popleft()

                inner.append(node.val)

                if node.left:
                    deque.append(node.left)

                if node.right:
                    deque.append(node.right)

            output.append(inner)

        return output
