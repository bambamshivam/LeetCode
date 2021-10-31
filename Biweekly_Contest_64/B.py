class Solution:
    def maxTwoEvents(self, l) -> int:
        n=len(l)
        l.sort(key=lambda x:x[0])
        b=[]
        for i in range(n):
            b.append(l[i][0])
        a=[0]*n;a[-1]=l[-1][2]
        for i in range(n-2,-1,-1):
            a[i]=max(l[i][2],a[i+1])
        m=0
        for i in range(n):
            t=bisect_left(b,l[i][1]+1)
            if t>=n:
                m=max(m,l[i][2])
            else:
                m=max(m,l[i][2]+a[t])
        return m