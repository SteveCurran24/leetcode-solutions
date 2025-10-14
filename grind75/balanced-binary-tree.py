# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def _height(self, root):
        if not root:
            return 0
        
        left_height = self._height(root.left)
        if left_height == -1:
            return -1
        
        right_height = self._height(root.right)
        if right_height == -1:
            return -1
        
        if abs(left_height - right_height) > 1:
            return -1
        
        return 1 + max(right_height, left_height)

    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        if self._height(root) == -1:
            return False
        else:
            return True
        
