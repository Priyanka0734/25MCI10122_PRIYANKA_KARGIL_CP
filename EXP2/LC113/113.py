# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        result = []

        def findPath(node, current_sum, path):
            if node is None:
                return

            path.append(node.val)
            current_sum += node.val

            if node.left is None and node.right is None:
                if current_sum == targetSum:
                    result.append(path[:])

            findPath(node.left, current_sum, path)
            findPath(node.right, current_sum, path)

            path.pop()

        findPath(root, 0, [])

        return result
        