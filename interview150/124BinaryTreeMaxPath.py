"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,None,None,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.


Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000

Going to add an assumption for larger arrays loading nodes: assu
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None, parent=None):
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




    @staticmethod
    def traverse_tree(root: Optional[TreeNode]) -> []:
        queue = [root]
        array_of_all_nodes = []
        array_of_all_nodes.append(root)
        while queue:
            current = queue.pop(0)
            print(current.val, end=" ")
            if current.left:
                queue.append(current.left)
                array_of_all_nodes.append(current.left)
            if current.right:
                queue.append(current.right)
                array_of_all_nodes.append(current.right)
        return array_of_all_nodes


    #The
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        def get_max_path(node: TreeNode) -> int:
            #for empty node
            if node.val is None:
                return 0
            if node.left is None and node.right is None:
                return node.val

            left_path_to_return = max(get_max_path(node.left), 0)
            right_path_to_return = max(get_max_path(node.right), 0)

            max_path = max(left_path_to_return, right_path_to_return)
            path_to_return = node.val + max_path

            self.max_sum = max(path_to_return, self.max_sum)
            return path_to_return

        get_max_path(root)
        return self.max_sum





solution = Solution()
values = [-10,9,20,15,7,4,5,62,4,5,7,8,6,34,5,7,45555555555,]
#values = [1,2,3]
root = solution.load_tree(values)
print(solution.maxPathSum(root))
