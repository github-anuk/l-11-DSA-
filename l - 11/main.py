class TEA:
    def __init__ (self,n):
        self.data=n
        self.left=None
        self.right=None
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
def insirt(root,x):
    if root is None:
        return TEA(x)
    elif root.data>x:
        root.left=insirt(root.left,x)
    else:
        root.right=insirt(root.right,x)
    return root

def delete(root,y):
    if root is None:
        return root
    if y<root.data:
        root.left =delete(root.left,y)
    elif y>root.data:
        root.right=delete(root.right,y)
    else:
        if root.left is None and root.right is None:
            return None
        elif root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right==None:
            temp = root.left
            root=None
            return temp
        temp=minValueNode(root.right)
        root.data=temp.data
        root.right=delete(root.right,temp.data)
    return root

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


l=int(input("HOW MUCH FOOD HAVE U GOT FOR TREE: "))
root=None
for i in range(l):
    m=int(input(f"FOOD {i+1} : "))
    root=insirt(root,m)
print("TREE BEFORE U TAKE STUFF OUT ")
inorder(root)

n=int(input("WHAT DO U WANT TO TAKE OUT: "))
root=delete(root,n)
inorder(root)