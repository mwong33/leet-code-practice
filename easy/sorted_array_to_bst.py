# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) space O(n) time
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        
        parent = TreeNode(nums[len(nums)//2])
        
        parent.left = self.sortedArrayToBST(nums[:len(nums)//2])
        parent.right = self.sortedArrayToBST(nums[len(nums)//2+1:])
        
        return parent
