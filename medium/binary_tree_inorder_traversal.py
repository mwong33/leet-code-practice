# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) time O(n) space if you count the array we are returning
    def inorderTraversalRecursion(self, root: TreeNode) -> List[int]:
        # inorder traversal - left, node, right
        # We can traverse the tree with in inorder traversal via recursion
        if root == None:
            return []
        
        left_sub_tree = self.inorderTraversalRecursion(root.left)
        right_sub_tree = self.inorderTraversalRecursion(root.right)
        
        return left_sub_tree + [root.val] + right_sub_tree
    
    # O(n) time O(n) space
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # inorder traversal - left, node, right
        # We can traverse the tree with DFS via a stack
        # 1) First keep adding left nodes to the stack.
        # 2) Once you cannot add anymore left nodes pop the stack and add it to our
        #    output array
        # 3) Add the right node to the stack if there is one and repeat step 1)
        # 4) If there is no right node to the stack, go to step 2
        if root == None:
            return []
        
        output_array = []
        stack = []
        seen = set()
        stack.append(root)
        
        while len(stack) != 0:
            current_node = stack[len(stack)-1]
            if current_node.left != None and current_node.left not in seen:
                stack.append(current_node.left)
            else:
                stack.pop()
                seen.add(current_node)
                output_array.append(current_node.val)
                if current_node.right != None:
                    stack.append(current_node.right)
                    
        return output_array
