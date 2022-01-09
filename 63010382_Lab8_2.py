class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
        self.height=1

    def __str__(self):
        return str(self.data)
class AVL:
    def __init__(self):
        self.root=None
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    def insert(self,root,data):
        if root==None:
            root=Node(data)
        else:
            if data<root.data:
                root.left=self.insert(root.left,data)
            else:
                root.right=self.insert(root.right,data)
        root.height=max(self.getHeight(root.left),self.getHeight(root.right))+1
        bl=self.getBalance(root)
        if bl>1 and data<root.left.data: #left left
            return self.rightRotate(root)
        if bl<-1 and data>=root.right.data: #right right
            return self.leftRotate(root)
        if bl>1 and data>=root.left.data: #left r ight
            root.left=self.leftRotate(root.left)
            return self.rightRotate(root)
        if bl<-1 and data<root.right.data: #right left
            root.right=self.rightRotate(root.right)
            return self.leftRotate(root)
        return root
    def inorder(self,root):
        if root!=None:
            self.inorder(root.right)
            print(root,end=' ')
            self.inorder(root.left)
    def getHeight(self,root):
        if not root:
            return 0
        else:
            return root.height
    def getBalance(self,root):
        if not root:
            return 0
        else:
            return self.getHeight(root.left)-self.getHeight(root.right)
    def leftRotate(self,z):
        y=z.right
        T2=y.left
        y.left=z
        z.right=T2
        z.height=(max(self.getHeight(z.left),self.getHeight(z.right)))+1
        y.height=(max(self.getHeight(y.left),self.getHeight(y.right)))+1
        return y
    def rightRotate(self,z):
        y=z.left
        T3=y.right
        y.right=z
        z.left=T3
        #reheight
        z.height=(max(self.getHeight(z.left),self.getHeight(z.right)))+1
        y.height=(max(self.getHeight(y.left),self.getHeight(y.right)))+1
        return y


if __name__ == "__main__":
    inp=list(map(int,input("Enter Input : ").split()))
    T=AVL()
    root=None
    for i in inp:
        root=T.insert(root,i)
        print('Insert : (',i,')')
        T.printTree(root)
        print('--------------------------------------------------')