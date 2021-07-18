class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        pre=points[0]
        m,n=len(points),len(points[0])
        for i in range(1,m):
            lft=[pre[0]]+[0]*(n-1)
            rgt=[0]*(n-1)+[pre[-1]]
            curr=[0]*n
            for j in range(1,n):
                lft[j]=max(lft[j-1]-1,pre[j])
            for j in range(n-2,-1,-1):
                rgt[j]=max(rgt[j+1]-1,pre[j])
            for j in range(n):
                curr[j]=points[i][j]+max(lft[j],rgt[j])
            pre=curr[:]
        return max(pre)