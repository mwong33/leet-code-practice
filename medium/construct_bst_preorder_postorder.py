# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n^2) time O(n) space
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        #Use pre to find root head an root.left
        #Use post to limit the index range of post for base case of recursion in addition to finding the size of the left subtree in order to find
        # root.right with pre
        return self.constructFromPrePostHelper(0, 0, len(post)-1, pre, post)
    
    def constructFromPrePostHelper(self, preStart, postStart, postEnd, pre, post):
        if len(pre) == 0 or preStart >= len(pre) or postStart > postEnd:
            return None
        
        root = TreeNode(pre[preStart])
        
        if postStart == postEnd:
            return root
        
        leftSubTreeEnd = 0
        
        for i in range(postStart, postEnd):
            if post[i] == pre[preStart+1]:
                leftSubTreeEnd = i
                break
                
        root.left = self.constructFromPrePostHelper(preStart + 1, postStart, leftSubTreeEnd, pre, post)
        root.right = self.constructFromPrePostHelper(preStart + (leftSubTreeEnd - postStart) + 2 , leftSubTreeEnd + 1, postEnd - 1, pre, post)
        
        return root
