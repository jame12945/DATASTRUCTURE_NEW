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
        if self.root == None:
            self.root = Node(data)
        else:
            cur = self.root
            while(1):
                if data < cur.data:
                    if cur.left != None:
                        cur = cur.left
                    else:
                        cur.left = Node(data)
                        return self.root
                else:
                    if cur.right != None:
                        cur = cur.right
                    else:
                        cur.right = Node(data)
                        return self.root

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def preOrder(self, node=-1):
        if node == -1:
            node = self.root
        if node != None:
            print(node.data, end=" ")
            self.preOrder(node.left)
            self.preOrder(node.right)

    def inOrder(self, node=-1):
        if node == -1:
            node = self.root
        if node != None:
            self.inOrder(node.left)
            print(node.data, end=" ")
            self.inOrder(node.right)

    def postOrder(self, node=-1):
        if node == -1:
            node = self.root
        if node != None:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print(node.data, end=" ")

    def breadth(self):
        q = list()
        q.append(self.root)
        while q:
            n = q.pop(0)
            print(n, end=" ")
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)

# T.printTree(root)
# print("===========================================================")
print("Preorder : ", end="")
T.preOrder()
print("\nInorder : ", end="")
T.inOrder()
print("\nPostorder : ", end="")
T.postOrder()
print("\nBreadth : ", end="")
T.breadth()