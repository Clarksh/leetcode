# https://blog.csdn.net/Findingxu/article/details/99640572

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        queue = [(root,0)] #初始化，里面放元组
        while(queue):
            node,depth = queue.pop(0) # 返回的不是元组(root,0)，而是两个元素
            if node:
                queue.append((node.left,depth+1))
                queue.append((node.right,depth+1))
                #queue.extend([(node.left,depth+1),(node.right,depth+1)])
        else:
            return depth