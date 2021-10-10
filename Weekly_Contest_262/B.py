class Solution:
    def minOperations(self, l, x: int) -> int:
        n=len(l);m=len(l[0])
        a=[]
        s=0
        for i in range(n):
            for j in range(m):
                a.append(l[i][j])
                s+=l[i][j]
        a.sort()
        def solve(k):
            t=0
            for i in range(n*m):
                t+=abs((a[i]-k)//x)
            return t
        for i in range(m*n-1):
            if (a[i+1]-a[i])%x!=0:
                return -1
        k=a[(n*m)//2]
        if (n*m)%2==1:
            return solve(k)
        else:
            return min(solve(k),solve(k-1))
        