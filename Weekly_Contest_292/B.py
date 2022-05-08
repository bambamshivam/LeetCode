# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root) -> int:
        ans=[0]
        def dfs(root):
            if not root:return [0,0]
            a=dfs(root.left);b=dfs(root.right)
            if (a[0]+b[0]+root.val)//(a[1]+b[1]+1)==root.val:ans[0]+=1
            return [a[0]+b[0]+root.val,a[1]+b[1]+1]
        dfs(root)
        return ans[0]