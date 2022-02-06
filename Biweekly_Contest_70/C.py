class Solution:
    def highestRankedKItems(self, grid: list[list[int]], pricing: list[int], start: list[int], t: int) -> list[list[int]]:
        n=len(grid);m=len(grid[0]);r=[0,1,0,-1,0];l=[];low,high=pricing
        v=[[0 for i in range(m)] for j in range(n)]
        q=deque();q.append([start[0],start[1],0]);v[start[0]][start[1]]=1
        while q:
            i,j,c=q.popleft()
            if low<=grid[i][j]<=high:l.append([c,grid[i][j],i,j])
            for k in range(4):
                if 0<=i+r[k]<n and 0<=j+r[k+1]<m and v[i+r[k]][j+r[k+1]]==0 and grid[i+r[k]][j+r[k+1]]>0:
                    q.append([i+r[k],j+r[k+1],c+1]);v[i+r[k]][j+r[k+1]]=1
        a=sorted(l);ans=[]
        for i in range(min(t,len(a))):ans.append([a[i][2],a[i][3]])
        return ans