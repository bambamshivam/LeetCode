class Solution:
    def maximalPathQuality(self, l, e, m: int) -> int:
        n=len(l)
        adj=[[] for i in range(n)]
        for i in range(len(e)):
            adj[e[i][0]].append([e[i][1],e[i][2]])
            adj[e[i][1]].append([e[i][0],e[i][2]])
        ans=[l[0]]
        def dfs(i,d,t,q):
            if t>m:
                return
            if i==0:
                ans[0]=max(ans[0],q)
            for j in adj[i]:
                s=q;c={};c=d.copy()
                if j[0] not in c:
                    s+=l[j[0]]
                    c[j[0]]=1
                dfs(j[0],c,t+j[1],s)
        d={};d[0]=1;dfs(0,d,0,l[0])
        return ans[0]