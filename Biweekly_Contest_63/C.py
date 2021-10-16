class Solution:
    def networkBecomesIdle(self, a,p) -> int:
        n=len(p)
        adj=[[] for i in range(n)]
        for i in range(len(a)):
            adj[a[i][0]].append(a[i][1])
            adj[a[i][1]].append(a[i][0])
        def bfs(i):
            q=deque()
            q.append(i)
            while q:
                r=q.popleft()
                for j in adj[r]:
                    if d[j]==-1:
                        d[j]=d[r]+1
                        q.append(j)
        d=[-1]*n;d[0]=m=0
        bfs(0)
        b=sorted(list(enumerate(d)),key=lambda x:x[1])
        for i in range(1,n):
            t=2*b[i][1]
            c=t//p[b[i][0]]
            if t%p[b[i][0]]==0:
                c-=1
            m=max(m,c*p[b[i][0]]+t)
        return m+1