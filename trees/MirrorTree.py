#User function Template for python3

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def areMirror(self,root1,root2):
        '''
        :param root1,root2: two root of the given trees.
        :return: True False
        
        '''
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        
        return (root1.data == root2.data and
                self.areMirror(root1.left,root2.right) and
                self.areMirror(root1.right,root2.left))
#User function Template for python3

