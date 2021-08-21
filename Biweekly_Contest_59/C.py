class Solution:
    def countPaths(self, n: int, roads) -> int:
        adj=[[] for i in range(n)]
        for i in roads:
            adj[i[0]].append([i[1],i[2]])
            adj[i[1]].append([i[0],i[2]])
        def mind(d,v):
            m=math.inf
            j=-1
            for i in range(n):
                if d[i]<m and v[i]==0:
                    m=d[i]
                    j=i
            return j
        d,v,p=[math.inf]*n,[0]*n,[0]*n
        d[0],p[0]=0,1
        for i in range(n):
            r=mind(d,v)
            if r>=0:
                v[r]=1
                for j in range(len(adj[r])):
                    if adj[r][j][1]+d[r]<d[adj[r][j][0]]:
                        d[adj[r][j][0]]=d[r]+adj[r][j][1]
                        p[adj[r][j][0]]=p[r]
                    elif adj[r][j][1]+d[r]==d[adj[r][j][0]]:
                        p[adj[r][j][0]]+=p[r]
        return p[-1]%(1000000007)
                
        