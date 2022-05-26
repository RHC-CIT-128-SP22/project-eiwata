

class Game_Iterator():

    def __init__(self, scene):
        self.left = None
        self.right = None
        self.scene = scene

    #insert node
    def insert(self, scene):
        if self.scene:
            if scene == self.scene+1:
                if self.left is None:
                    self.left = Game_Iterator(scene)
                else:
                    self.left.insert(scene)
            else:
                if self.right is None:
                    self.right = Game_Iterator(scene)
                else:
                    self.right.insert(scene)
        else:
            self.scene = scene

    #print the tree
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.scene)
        if self.right:
            self.right.printTree()

    #inorder traversal
    #left -> root -> right
    def inorderTraversal(self, node):
        res = []
        if node:
            res = self.inorderTraversal(node.left)
            res.append(node.scene)
            res = res + self.inorderTraversal(node.right)
        return res


story = Game_Iterator(1)
story.insert(2)
story.insert(3)
story.insert(4)
story.insert(5)
print(story.inorderTraversal(story))

