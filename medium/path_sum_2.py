# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n^2) O(h) space where h is the height of the tree and n is the number of nodes
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:        
        return self.dfs(root, targetSum, 0)
        
    def dfs(self, root, target_sum, current_sum):
        if root == None:
            return []
        
        current_sum += root.val
        
        # Base Case
        if root.left == None and root.right == None:
            if current_sum == target_sum:
                return [[root.val]]
            else:
                return []
        
        left_result = self.dfs(root.left, target_sum, current_sum)
        right_result = self.dfs(root.right, target_sum, current_sum)

        for index in range(len(left_result)):
            left_result[index] = [root.val] + left_result[index]
        
        for index in range(len(right_result)):
            right_result[index] = [root.val] + right_result[index]
            
        return left_result + right_result
