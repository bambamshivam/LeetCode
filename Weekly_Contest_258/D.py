class Solution:
    def smallestMissingValueSubtree(self, p, l):
        n=len(p)
        adj=[[] for i in range(n)]
        v=[0]*100050
        ans=[1]*n
        if 1 not in l:
            return ans
        for i in range(1,n):
            adj[p[i]].append(i)
        def dfs(i):
            if v[l[i]]==0:
                for j in range(len(adj[i])):
                    dfs(adj[i][j])
                v[l[i]]=1
        i=l.index(1)
        t=1
        while i>=0:
            dfs(i)
            while v[t]==1:
                t+=1
            ans[i]=t
            i=p[i]
        return ans
            
        