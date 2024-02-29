'''
Given the root of a binary tree, return the length of the longest path,
where each node in the path has the same value. This path may or may not pass through the root.
The length of the path between two nodes is represented by the number of edges between them.
'''

'''
intuition:
We will maintain following variables:
global: max_val which will always have the max value.
local: cur_val which will compute the value at the node.
local: ret_val which will compute the value to be returned to parent.

To compute the solution of this question we have to consider 4 possible conditions at each level.

if left_child.val == right_child.val == root.val
   4
 /    \
4      4
		\
		 4
In this case,
cur_val = lval + rval + 2 (+ 2 because two paths are now added from right and left)
ret_val = max(lval, rval) + 1 (because we can only send one path to the parent. To get the longest path we will have to send the max(lval, rval)

if only left_child.val == root.val
   4
 /    \
4      5
cur_val = ret_val = lval + 1
3. If only right_child.val == root.val

   5
 /    \
4      5
cur_val = ret_val = rval + 1
4. If both right_child and left_child don't match with root.val

   3
 /    \
4      5
cur_val = ret_val = 0 Since there no path between the child and parent node.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:return 0
        self.ans = 0
        self.postOrder(root)
        return self.ans
    def postOrder(self,node):
        if not node: return 0
        l_cnt, r_cnt = 0, 0
        
        l_cnt = self.postOrder(node.left)
        r_cnt = self.postOrder(node.right)

        if node.left and node.right and (node.val == node.left.val == node.right.val):
            self.ans = max(self.ans,l_cnt + r_cnt + 2)
        
        elif node.left and (node.left.val == node.val):
            l_cnt += 1
            self.ans = max(self.ans,l_cnt)

        elif node.right and (node.right.val == node.val):
            r_cnt += 1
            self.ans = max(self.ans,r_cnt)
            return r_cnt
        else:
            return 0