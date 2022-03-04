class Node:
    def __init__(self, valueInput):
        self.value = valueInput
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, valueInput):
        self.root = Node(valueInput)
    def addNode(self,valueInput):
        newNode = Node(valueInput)
        runner = self.root
        while runner:
            if newNode.value < runner.value:
                if runner.left == None:
                    runner.left = newNode
                    return self
                else:
                    runner = runner.left
            else:
                if runner.right == None:
                    runner.right = newNode
                    return self
                else:
                    runner = runner.right
    def contains(self, valueInput):
        runner = self.root
        while runner:
            if valueInput == runner.value:
                return True
            else:
                if valueInput < runner.value:
                    if runner.left == None:
                        return False
                    else: 
                        runner = runner.left
                else:
                    if runner.right == None:
                        return False
                    else:
                        runner = runner.right
    def min(self):
        runner = self.root
        while runner:
            if runner.left == None:
                return runner.value
            else:
                runner = runner.left
    def max(self):
        runner = self.root
        while runner:
            if runner.right == None:
                return runner.value
            else:
                runner = runner.right

myTree = BinaryTree(7)

print(myTree.addNode(4).addNode(2).addNode(8).max())