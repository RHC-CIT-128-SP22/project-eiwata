

class Scene_Tracker():

    def __init__(self, scene):
        self.left = None
        self.right = None
        self.scene = scene

    #insert node
    def insert(self, scene):
        if self.scene:
            if scene < self.scene:
                if self.left is None:
                    self.left = Scene_Tracker(scene)
                else:
                    self.left.insert(scene)
            elif scene > self.scene:
                if self.right is None:
                    self.right = Scene_Tracker(scene)
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
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.scene)
            res = res + self.inorderTraversal(root.right)
        return res


story = Scene_Tracker('A')
story.insert('B')
story.insert('C')
story.insert('D')
story.insert('E')
story.insert('e')
story.insert('f')
print(story.inorderTraversal(story))

