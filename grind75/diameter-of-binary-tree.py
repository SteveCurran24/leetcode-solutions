# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def height(self, root):
        if root is None:
            return 0
        
        lheight = self.height(root.left)
        rheight = self.height(root.right)
        new_diameter = lheight + rheight

        if self.diameter < new_diameter:
            self.diameter = new_diameter

        return max(lheight, rheight) + 1

    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.diameter = 0
        self.height(root)
        return self.diameter
