### Breadth first search of a tree


# Definition for a binary tree node.
class BinaryTreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = BinaryTreeNode(5)
root.left = BinaryTreeNode(4)
root.right = BinaryTreeNode(7)
root.left.left=BinaryTreeNode(12)
root.left.right=BinaryTreeNode(11)
root.right.left=BinaryTreeNode(23)
root.right.right=BinaryTreeNode(25)



class BFS:
    def print(self, root):
        queue = []

        queue.append(root.right)
        queue.append(root.left)


