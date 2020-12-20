# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) space O(n) time
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        
        level_dict = {root: 0}
        
        queue = deque()
        queue.append(root)
        
        bfs_array = []
        
        while len(queue) != 0:
            current_node = queue.popleft()
            bfs_array.append(current_node)
            # Add children to queue AND Add children to dictionary
            if current_node.left != None:
                queue.append(current_node.left)
                level_dict[current_node.left] = level_dict[current_node] + 1
            
            if current_node.right != None:
                queue.append(current_node.right)
                level_dict[current_node.right] = level_dict[current_node] + 1
                
        final_array = []
        temp_array = []
        current_level = 0
                
        for i in range(len(bfs_array)):
            print(i, bfs_array[i].val)
            level = level_dict[bfs_array[i]]
            
            if level != current_level:
                final_array.append(temp_array)
                temp_array = []
                current_level += 1
            temp_array.append(bfs_array[i].val)
            
        final_array.append(temp_array)
            
        return final_array
