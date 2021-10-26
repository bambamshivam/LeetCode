class Solution:
    def minimumTime(self, n: int, relations, time) -> int:
        d={}
        for i in range(n):
            d[i]={}
        for i in relations:
            d[i[0]-1][i[1]-1]=1
        s=[];v=[0]*n
        def solve(r):
            v[r]=1
            for i in d[r]:
                if v[i]==0:
                    solve(i)
            s.append(r)
        for i in range(n):
            if v[i]==0:
                solve(i)
        s=s[::-1];p=[0]*n
        for i in s:
            for j in d[i]:
                p[j]=max(p[j],p[i]+time[i])
        m=0
        for i in range(n):
            m=max(m,p[i]+time[i])
        return m