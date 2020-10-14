import numpy as np

h=8 #по горизонтали
v=8 #по вертикали


def create_board(h,v):
    ch = np.zeros((h,v,2))
    for i in range(h):
        for j in range(v):
            #ch[i][j] = np.zeros(2)
            ch[i][j][0] = 0
            ch[i][j][1] = 1 

    return ch
ch = create_board(h,v)
fig = np.array([1,2,3])
fig2 = np.array([4,5,6])
qw = [1,2,3]
#fig[0] = qw

myTree = ['a', ['b', ['d',[],[]], ['e',[],[]] ], ['c', ['f',[],[]], []] ]

def BinaryTree(r):
    return [r, [], []]
#print(myTree)
#print(myTree[2])

a, b, c, d, e, f, g, h = range(8)
N = [
	{b, c, d, e, f}, # a
	{c, e}, # b
	{d}, # c
	{e}, # d
	{f}, # e
	{c, g, h}, # f
	{f, h}, # g
	{f, g} # h
]
print(N)
print(b in N[a])  # смежная?
print(len(N[f]))

class Tree:
	def __init__(self, left, right):
		self.left = left
		self.right = right
t = Tree(Tree("a", "b"), Tree("c", "d"))
print(t.right.left)

class TreeNode:
    def __init__(self,key,val,left=None,right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self
#print(ch)