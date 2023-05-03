class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def insert(root, newValue):
    # if binary search tree is empty, create a new node and declare it as root
    if root is None:
        root = BinaryTreeNode(newValue)
        return root
    # if newValue is less than value of data in root, add it to left subtree and proceed recursively
    if newValue < root.data:
        root.leftChild = insert(root.leftChild, newValue)
    else:
        # if newValue is greater than value of data in root, add it to right subtree and proceed recursively
        root.rightChild = insert(root.rightChild, newValue)
    return root

def imprime(node):
    if node == None:
        return
    print("Nodo:" + str(node.data))

    if node.leftChild != None:
        print("Hijo izquierdo:" + str(node.leftChild.data))

    if node.rightChild != None:
        print("Hijo derecho:" + str(node.rightChild.data))

    imprime(node.leftChild)
    imprime(node.rightChild)


root = insert(None, 50)
insert(root, 20)
insert(root, 53)
insert(root, 11)
insert(root, 22)
insert(root, 52)
insert(root, 78)

imprime(root)