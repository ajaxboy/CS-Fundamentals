#6:42
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def preorder(self):
       
        if not self.data:
            return

        data.append(self.data)

        if self.left:
            self.left.preorder()

        if self.right:
            self.right.preorder()

        return data
    def inorder(self):
        inorder.data = []
        if not self.data:
            return

        if self.left:
            self.left.inorder()

        data.append(self.data)

        if self.right:
            self.right.inorder()

        return inorder.data   

    def postorder(self):
        postorder.data = []
        if not self.data:
            return

        if self.left:
            self.left.postorder()

        if self.right:
            self.right.postorder()   

        data.append(self.data)

        return postorder.data

root = Node(21)
root.left = Node(15)
root.left.left = Node(5)
root.left.right = Node(9)
root.right = Node(29)
root.right.left = Node(30)
root.right.right = Node(40)


print(root.inorder())
print(root.preorder())
print(root.postorder())

    