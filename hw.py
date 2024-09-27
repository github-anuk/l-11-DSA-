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
def preorder(root):
    if root:
        print(root.data)
        inorder(root.left)
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)

def search(root,m):
    if root.data==m:
        return root
    elif root.data >m and root.left is not None:
        return search(root.left,m)
    elif root.data < m and root.right is not None:
        return search(root.right,m)     
    else:
        return -1
    
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
print("FORST TREE :  ")
a=input("WHICH KIND OF TRANSVERAL DO YOU WANT (INORDER),(PREORDER) OR (POSTORDER) : ")
if a=="inorder":
    inorder(root)
elif a=="preorder":
    preorder(root)
elif a=="postorder":
    postorder(root)
else:
    print("NO SUCH THING EXISTS")

se=input("DO U WANT TO SEARCH VALUES(YES OR NO): ")
if se == "yes":
    m=int(input("what do u want to search: "))
    s=search(root,m)
    if s==-1:
        print("NOT FOUND")
    else:
        print("FOUND",m)
else:
    print("ok ")

n=input("DO U WANT TO DELETE SOMETHING: ")
if n=="yes":
    no=int(input("WHAT DO U WANT TO DELETE : "))
    root=delete(root,no)
    inorder(root)
else:
    print("OK BYEEEEEEE")