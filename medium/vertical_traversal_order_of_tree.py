# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n + wlogw + w*hlogh) time O(h + w*h) space => O(nlogn) time O(n) space
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        data = {}
        self.preOrder(root, 0, 0, data)
        keys = list(data.keys())
        keys.sort()
        
        output = []
        for key in keys:
            data[key].sort()
            temp_list = []
            for number in data[key]:
                temp_list.append(number[1])
            output.append(temp_list)
            
        return output
        
    def preOrder(self, root, x, y, data):
        # Base Case
        if root == None:
            return
        
        if x not in data:
            data[x] = [(y, root.val)]
        else:
            data[x].append((y, root.val))
        
        self.preOrder(root.left, x-1, y+1, data)
        self.preOrder(root.right, x+1, y+1, data)
        
"""
(y value, value)

NLR

1: {"0": [1]}
2: {"0": [1], "-1": [2]}
3: {"0": [1], "-1": [2], "-2": [4]}
4: {"0": [1, 5], "-1": [2], "-2": [4]}
5: {"2": [7] 1": [3], 0": [1, 5, 6], "-1": [2], "-2": [4]}

1: {"0": [3]}
2: {"0": [3], "-1": [9]}
3: {"2": [7], "1": [20] "0": [3, 15], "-1": [9]}

"""
