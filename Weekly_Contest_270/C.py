# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root, s: int, d: int) -> str:
        p={};s1=[None];d1=[None]
        def solve(root):
            if root==None: return
            if root.val==s: s1[0]=root
            if root.val==d: d1[0]=root
            if root.left: p[root.left]=root
            if root.right: p[root.right]=root
            solve(root.right);solve(root.left)
        solve(root);h=s1[0];la=set();l=[];a="";la.add(h);l.append(h);h1=d1[0];b=""
        while h.val!=root.val:
            la.add(p[h])
            l.append(p[h])
            h=p[h]
        while h1 not in la:
            if p[h1].left==h1:
                b+='L'
            else:
                b+='R'
            h1=p[h1]
        return 'U'*l.index(h1)+b[::-1]