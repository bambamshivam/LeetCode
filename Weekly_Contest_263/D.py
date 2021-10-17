class Solution:
    def secondMinimum(self, n: int, edges, time: int, change: int) -> int:
        adj=[[] for i in range(n)]
        for i in edges:
            adj[i[0]-1].append(i[1]-1)
            adj[i[1]-1].append(i[0]-1)
        d=[[] for i in range(n)];d[0]=[0]
        h=[(0,0)]
        while h:
            r=heappop(h)
            if r[1]==n-1 and len(d[r[1]])==2:
                return max(d[r[1]])
            for i in adj[r[1]]:
                if (r[0]//change)%2==0:
                    c=r[0]+time
                else:
                    c=ceil(r[0]/(2*change))*(2*change) + time
                if len(d[i])==0 or (len(d[i])==1 and c!=d[i][0]) or (len(d[i])==2 and c<max(d[i]) and c!=min(d[i])):
                    d[i].append(c)
                    heappush(h,(c,i))
                if len(d[i])==3:
                    d[i].remove(max(d[i]))
                    
            