class Solution:
    def findFarmland(self, land):
        n=len(land)
        m=len(land[0])
        v=[[0 for i in range(m)] for j in range(n)]
        def dfs(land,i,j,m1,co,v):
            v[i][j]=1
            if i+j>m1[0]:
                m1[0]=i+j
                co[0]=i
                co[1]=j
            r=[1,-1,0,0]
            c=[0,0,1,-1]
            for k in range(4):
                if 0<=i+r[k]<n and 0<=j+c[k]<m and v[i+r[k]][j+c[k]]==0 and land[i+r[k]][j+c[k]]==1:
                    dfs(land,i+r[k],j+c[k],m1,co,v)
        a=[]
        for i in range(n):
            for j in range(m):
                if v[i][j]==0 and land[i][j]==1:
                    co=[i,j]
                    m1=[i+j]
                    dfs(land,i,j,m1,co,v)
                    a.append([i,j,co[0],co[1]])
        return a
        
        