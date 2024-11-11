"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:


    def load_tree(self, values, nodes_to_load=[]):
        first_node = None
        if not nodes_to_load:
            first_node = TreeNode(values.pop(0))
            nodes_to_load.append(first_node)
        new_node_level = []
        while values:
            for node in nodes_to_load:
                if values:
                    node.left = TreeNode(values.pop(0))
                    node.left.parent = node
                    new_node_level.append(node.left)
                if values:
                    node.right = TreeNode(values.pop(0))
                    node.right.parent = node
                    new_node_level.append(node.right)
            nodes_to_load = new_node_level

        if first_node is not None:
            return first_node

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_level = -1

        def get_queue_depth(node: TreeNode, level=1):
            if(node is None):
                self.max_level = max(self.max_level, level)
                return
            level = level + 1
            if(node.left is None and node.right is None):
                self.max_level = max(self.max_level, level)
                return
            get_queue_depth(node.left, level)
            get_queue_depth(node.right, level)
        get_queue_depth(root.left)
        get_queue_depth(root.right)

        return self.max_level


solution = Solution()
values = [1,2,2,3,3,3,3,4,4,4,4,4,4,4,4,5]
#values = [1,2,3]
root = solution.load_tree(values)
print(solution.maxDepth(root))