class Solution:
    def platesBetweenCandles(self, s: str, q):
        n=len(s)
        a=[];b=[0]*(n+1)
        for i in range(n):
            if s[i]=='|': a.append(i)
        for i in range(n):
            if s[i]=='*':
                b[i+1]=b[i]+1
            else:
                b[i+1]=b[i]
        ans=[]
        for i in range(len(q)):
            t1=bisect_left(a,q[i][0])
            t2=bisect_right(a,q[i][1])
            t2-=1
            if t1>=n: t1-=1
            if t1>t2:
                ans.append(0);continue
            ans.append(b[a[t2]+1]-b[a[t1]])
        return ans