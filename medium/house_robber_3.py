# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Top Down Memo - O(n) time O(n) space where n is the number of nodes
    def rob(self, root: TreeNode) -> int:
        return max(self.robMemo(root, True, {}), self.robMemo(root, False, {}))
    
    def robMemo(self, root, chosen, cache):
        if (root, chosen) in cache:
            return cache[(root, chosen)]
        
        # Base Case
        if root == None:
            return 0

        if chosen:
            ignore_left = self.robMemo(root.left, False, cache)
            ignore_right = self.robMemo(root.right, False, cache)
            
            cache[(root, chosen)] = root.val + ignore_left + ignore_right
            return cache[(root, chosen)]
        else:
            ignore_left = self.robMemo(root.left, False, cache)
            ignore_right = self.robMemo(root.right, False, cache)
            choose_left = self.robMemo(root.left, True, cache)
            choose_right = self.robMemo(root.right, True, cache)
            
            cache[(root, chosen)] = max(ignore_left + ignore_right, choose_left + choose_right, ignore_left + choose_right, choose_left + ignore_right)
            return cache[(root, chosen)]
