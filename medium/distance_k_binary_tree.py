# O(n) time O(n) space
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeParentNode:
    def __init__(self, val, parent):
        self.val = val
        self.parent = parent
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        # Find the target node and its ancestor (if there is one) with DFS
        if root.val == target.val:
            return self.getDistanceKChildren(root, K)
        
        # Create cache
        cache = {}
        self.createCache(root, None, cache)
        
        # Create our output array 
        output_array = self.getDistanceKChildren(target, K)
        
        # Add ancestor nodes to our output_array
        ancestor = cache[target]
        current_target = target
        while (K-1) >= 0 and ancestor != None:
            output_array += self.getDistanceKAncestor(ancestor, current_target, K-1)
            current_target = ancestor
            ancestor = cache[ancestor]
            K -= 1
        
        return output_array
            
    def createCache(self, node, parent, cache):
        if node == None:
            return
        
        cache[node] = parent
        self.createCache(node.left, node, cache)
        self.createCache(node.right, node, cache)
        
    def getDistanceKAncestor(self, ancestor, target, distance):
        if distance == 0:
            return [ancestor.val]
        
        correct_node = None
        if ancestor.left == target:
            correct_node = ancestor.right
        else:
            correct_node = ancestor.left
        
        if correct_node != None:
            return self.getDistanceKChildren(correct_node, distance-1)
        else:
            return []
    
    def getDistanceKChildren(self, root, k):
        current_level = [root]
        current_level_val = [root.val]
        next_level = []
        next_level_val = []
        level = 0
        
        while level < k and len(current_level) != 0:
            current_node = current_level.pop()
            
            if current_node.left != None:
                next_level.append(current_node.left)
                next_level_val.append(current_node.left.val)
            if current_node.right != None:
                next_level.append(current_node.right)
                next_level_val.append(current_node.right.val)
                
            if len(current_level) == 0:
                current_level = next_level
                current_level_val = next_level_val
                next_level = []
                next_level_val = []
                level += 1
            
        return current_level_val
            
    
