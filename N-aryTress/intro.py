#properties of generic tree ---> many children at every node  and the number of nodes not known in advance
# hence we can use the standard way of allocating tree nodes
'''so for storing the addresses of the child node we can use arrays or LLs but in LLs we cant randomly access and in array 
we need to use the dynamic arrays which would be better but not an efficient one
Efficient approach:--firstchild and in the firstchild sibling representation folllowing steps are taken'''
# Python program to find the height of 
# an N-ary tree 
from collections import defaultdict, deque
# Structure of a node of an n-ary tree 
class Node: 
  def __init__(self, val): 
    self.val = val
    self.children = [] 

# Utility function to create a new tree node 
def new_node(val): 
  node = Node(val) 
  return node 

# Function that will return the depth 
# of the tree 
def maxDepth(node): 
  # Base case 
  if node is None: 
    return 0

  # Check for all children and find 
  # the maximum depth 
  maxdepth = 0
  for child in node.children: 
    maxdepth = max(maxdepth, maxDepth(child)) 

  return maxdepth + 1

#preorder recurisve
def preorder(root):
  ans = []
  def dfs(node):
      if not node:
          return
      ans.append(node.val)
      for child in node.children:
          dfs(child)
  dfs(root)
  return ans
#def preorder iterative
def preorder_iter(root):
  if not root:
      return []
  q = deque([root])
  ans = []

  while q:
      child = q.popleft()
      ans.append(child.val)
      for c in reversed(child.children):
          q.appendleft(c)
  return ans

def postorder(root):
  if not root:
    return []
  stack = [root]
  ans= []
  while stack:
    node = stack.pop()
    ans.append(node.val)
    for child in node.children:
      stack.append(child)
  return ans[::-1]

def levelorder(root):
  ans =  defaultdict(list)
  def dfs(node,level):
    if not node:
      return
    ans[level].append(node.val)
    for child in node.children:
      dfs(child,level+1)
  dfs(root,0)
  return [ value for key,value in sorted(ans.items())]

# Driver program 
if __name__ == '__main__': 
  """ Let us create below tree 
      A 
    / / \ \ 
    B F D E 
    / \ | /|\ 
    K J G C H I 
    /\		 \ 
    N M		 L 
  """

  root = new_node('A') 
  root.children.extend([new_node('B'), new_node('F'), new_node('D'), new_node('E')]) 
  root.children[0].children.extend([new_node('K'), new_node('J')]) 
  root.children[2].children.append(new_node('G')) 
  root.children[3].children.extend([new_node('C'), new_node('H'), new_node('I')]) 
  root.children[0].children[0].children.extend([new_node('N'), new_node('M')]) 
  root.children[3].children[2].children.append(new_node('L')) 

  print(maxDepth(root)) 
  print(preorder(root))
  print(postorder(root))
  print(levelorder(root))
        