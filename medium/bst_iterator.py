# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def convertToInOrderArray(root):
    if root == None:
        return []
    
    left_array = convertToInOrderArray(root.left)
    right_array = convertToInOrderArray(root.right)
    
    return left_array + [root.val] + right_array

# O(n) init time. O(1) next time and O(1) hasNext time
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.inorder_array = convertToInOrderArray(root)
        self.index = -1
        
    def next(self) -> int:
        self.index += 1
        
        return self.inorder_array[self.index]

    def hasNext(self) -> bool:
        if self.index == len(self.inorder_array) - 1:
            return False
        
        return True


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
