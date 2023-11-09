# BinaryTree
#       '+'
#    /       \
#   'a'      '*'
#           /   \
#         'b'   '-'
#              /   \
#            '/'   'e'
#            /  \
#          'c'  'd'

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self, data=None):
        if data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    def simetric_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            print('(', end='')
            self.simetric_traversal(node.left)
        print(node, end='')
        if node.right:
            self.simetric_traversal(node.right)
            print(')',end='')
    def posOrder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.posOrder_traversal(node.left)
        if node.right:
            self.posOrder_traversal(node.right)
        print(node)
        
     def height(self, node=None):
        if node is None:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.height(node.left)
        if node.right:
            hright = self.height(node.right)
        if hright > hleft:
            return hright + 1
        return hleft + 1
    
if __name__ == "__main__":
    # tree = BinaryTree(7)
    # tree.root.left = Node(18)
    # tree.root.right = Node(14)
    # print(tree.root)
    # print(tree.root.left)
    # print(tree.root.right)
    tree = BinaryTree()
    n1 = Node('a')
    n2 = Node('+')
    n3 = Node('*')
    n4 = Node('b')
    n5 = Node('-')
    n6 = Node('/')
    n7 = Node('c')
    n8 = Node('d')
    n9 = Node('e')

    n6.left = n7
    n6.right = n8
    n5.left = n6
    n5.right = n9
    n3.left = n4
    n3.right = n5
    n2.left = n1
    n2.right = n3

    tree.root = n2
    tree.simetric_traversal()
    print()

    tree2 = BinaryTree()
    n1 = Node('i')
    n2 = Node('n')
    n3 = Node('s')
    n4 = Node('c')
    n5 = Node('r')
    n6 = Node('e')
    n7 = Node('v')
    n8 = Node('a')
    n9 = Node('-')
    n10 =Node('5')
    n0 = Node('3')
    
    n0.left = n6
    n0.right = n10
    n6.left = n1
    n6.right = n5
    n5.left = n2
    n5.right = n4
    n4.right = n3
    n10.left = n8
    n10.right = n9 
    n8.right = n7

    tree2.root = n0
    tree2.posOrder_traversal()
    print("Altura da árvore: ", tree.height())
