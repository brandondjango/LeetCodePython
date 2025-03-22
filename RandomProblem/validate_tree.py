#You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.
#
#If node i has no left child then leftChild[i] will equal -1, similarly for the right child.
#
#Note that the nodes have no values and that we only use the node numbers in this problem.
#
#
#
#Example 1:
#
#
#Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
#Output: true
#Example 2:
#
#
#Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
#Output: false
#Example 3:
#
#
#Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
#Output: false
#
from collections import defaultdict
from symtable import Class
from typing import List



class Solution:
    @staticmethod
    def validateBinaryTreeNodes(n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parentHash = defaultdict(lambda: False)
        childrenHash = defaultdict(lambda: None)
        #assume lists are same length
        for i in range(len(leftChild)):

            #two parents
            if leftChild[i] >= 0:
                if parentHash[leftChild[i]] is not False:
                    return False
                else:
                    parentHash[leftChild[i]] = i
            if rightChild[i] >= 0:
                if parentHash[rightChild[i]] is not False:
                    return False
                else:
                    parentHash[rightChild[i]] = i


            #more than 2 children
            if leftChild[i] > -1:
                if childrenHash[i] is None:
                    childrenHash[i]=0
                childrenHash[i] += 1
                if childrenHash[i] > 2:
                    return False

            if rightChild[i] > -1:
                if childrenHash[i] is None:
                    childrenHash[i]=0
                childrenHash[i] += 1
                if childrenHash[i] > 2:
                    return False
            print("parent")
            print(parentHash)
            print("children")
            print(childrenHash)

        for i in range(len(leftChild)):
            if parentHash[i] is False and childrenHash[i] is None:
                return False;
        return True

leftChildren = [1,-1,3,-1]
rightChildren = [2,3,-1,-1]

print(Solution.validateBinaryTreeNodes(n=4, leftChild=leftChildren, rightChild=rightChildren))