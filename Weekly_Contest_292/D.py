class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        n=len(grid);m=len(grid[0]);c=d=0
        dp=[[set() for i in range(m)] for j in range(n)]
        for i in range(n):
            c+=1 if grid[i][0]=='(' else -1
            if c>=0:dp[i][0].add(c)
            else:break
        for i in range(m):
            d+=1 if grid[0][i]=='(' else -1
            if d>=0:dp[0][i].add(d)
            else:break
        for i in range(1,n):
            for j in range(1,m):
                a=1 if grid[i][j]=='(' else -1
                for e in dp[i-1][j]:
                    if e+a>=0:dp[i][j].add(e+a)
                for e in dp[i][j-1]:
                    if e+a>=0:dp[i][j].add(e+a)
        return len(dp[n-1][m-1])>0 and 0 in dp[n-1][m-1]