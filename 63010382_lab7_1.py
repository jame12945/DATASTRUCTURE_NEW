class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        newNode = Node(data)
        if self.root is None:
            self.root = newNode
        else:  # others case
            ctn = self.root
            while True:
                if data >  ctn.data:
                    if  ctn.right is None:
                        ctn.right = newNode
                        break
                    ctn =  ctn.right

                elif data <  ctn.data:
                    if  ctn.left is None:
                        ctn.left = newNode
                        break
                    ctn =  ctn.left

        return self.root

    def printTree(self, node, level=0):
        if node is None:
            return
        self.printTree(node.right, level + 1)
        print('     ' * level, node.data)
        self.printTree(node.left, level + 1)


inp = [int(i) for i in input('Enter Input : ').split()]

tree = BST()

for i in inp:
    root = tree.insert(i)

tree.printTree(root)