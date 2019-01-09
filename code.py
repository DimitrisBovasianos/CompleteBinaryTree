class Node(object):
    def __init__(self,data):
        self.root = data
        self.left = None
        self.right = None

    def has_2_childs(self):
        if self.left and self.right:
            return True
        else:
            return None

class BST(object):
    def __init__(self):
        self.top = None

    def recrsBST(self, node, data):
        if node is None:
            node = Node(data)
        elif node.left is None:
            node.left = self.recrsBST(node.left,data)
        elif node.right is None:
            node.right = self.recrsBST(node.right,data)
        elif node.left.has_2_childs() and not node.right.has_2_childs():
            node.right = self.recrsBST(node.right,data)
        else:
            node.left = self.recrsBST(node.left,data)
        return node
    def insert(self,data):
        self.top = self.recrsBST(self.top, data)


    def findvisible(self,root):
        if root is None:
            return 0
        max = root.root
        count = 1
        if root.left and root.left.root > max:
            count = self.findvisible(root.left)+self.findvisible(root.right) + 1
        if  root.right and root.right.root > max:
            count = self.findvisible(root.left) + self.findvisible(root.right) +1
        return count
