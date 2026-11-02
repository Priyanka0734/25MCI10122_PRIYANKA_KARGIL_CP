# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxSumBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.ans = 0

        def solve(node):
            if node is None:
                return True, float('inf'), float('-inf'), 0

            left_bst, left_min, left_max, left_sum = solve(node.left)
            right_bst, right_min, right_max, right_sum = solve(node.right)

            if left_bst and right_bst and left_max < node.val < right_min:
                curr_sum = left_sum + right_sum + node.val

                self.ans = max(self.ans, curr_sum)

                return (
                    True,
                    min(left_min, node.val),
                    max(right_max, node.val),
                    curr_sum
                )

            return False, 0, 0, 0

        solve(root)

        return self.ans

        