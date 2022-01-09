class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


def preOrder(node):
    if node != None:
        print(node.data, end="")
        preOrder(node.left)
        preOrder(node.right)


def inOrder(node):
    if node != None:
        p = True
        if node.left == None and node.right == None:
            p = False
        if p:
            print("(", end="")
        inOrder(node.left)
        print(node.data, end="")
        inOrder(node.right)
        if p:
            print(")", end="")


def postOrder(node):
    if node != None:
        postOrder(node.left)
        postOrder(node.right)
        print(node.data, end="")


def breadth(self):
    q = list()
    q.append(self.root)
    while len(q) != 0:
        n = q.pop(0)
        print(n, end=" ")
        if n.left:
            q.append(n.left)
        if n.right:
            q.append(n.right)


def printTree(node, level=0):
    if node != None:
        printTree(node.right, level + 1)
        print('     ' * level, node)
        printTree(node.left, level + 1)


s = list()
inp = input('Enter Postfix : ')

for i in inp:
    if 'a' <= i <= 'z':
        s.append(Node(i))
    elif i in "+-*/":
        a = s.pop()
        b = s.pop()
        root = Node(i, b, a)
        s.append(root)

print("Tree :")
printTree(root)
print("--------------------------------------------------")
print("Infix : ", end="")
inOrder(root)
print("\nPrefix : ", end="")
preOrder(root)

