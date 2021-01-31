# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodesHorrible(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:        
        # Convert our list to a set
        to_delete_set = set()
        
        for number in to_delete:
            to_delete_set.add(number)
            
        # DFS
        return self.dfs(root, to_delete_set, root)
        
    def dfs(self, root, to_delete_set, parent):
        # Base Case
        if root == None:
            if parent == None:
                return []
            else:
                return [parent]
            
        # Check if your children are to be deleted
        left_pointer = root.left
        right_pointer = root.right
        
        if root.left != None and root.left.val in to_delete_set:
            root.left = None
        if root.right != None and root.right.val in to_delete_set:
            root.right = None
                        
        # Check if you yourself are to be deleted
        if root.val in to_delete_set:
            left_result = self.dfs(left_pointer, to_delete_set, left_pointer) 
            right_result = self.dfs(right_pointer, to_delete_set, right_pointer)
            root.left = None
            root.right = None
            
            return self.unique(left_result, right_result)
        else:
            left_result = self.dfs(left_pointer, to_delete_set, parent) 
            right_result = self.dfs(right_pointer, to_delete_set, parent)
            
            result = self.unique(left_result, right_result)
            return self.unique(result, [parent])
        
    def unique(self, list_a, list_b):
        unique = set()
        
        for index in range(len(list_a)):
            unique.add(list_a[index])
            
        for index in range(len(list_b)):
            unique.add(list_b[index])
            
        return list(unique)
        
"""
1) Parent of deleted node must lose that connection
2) When we find a node to delete
   Check if they have children. If so, return the root.left and/or root.right
"""
