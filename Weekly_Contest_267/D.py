class Solution:
    def friendRequests(self, n: int, a, b) :
        ans=[]
        adj=[[] for i in range(n)]
        def dfs(t,i,v):
            v[i]=t
            for j in adj[i]:
                if v[j]==0:
                    dfs(t,j,v)
        def solve(v):
            t=1
            for i in range(len(v)):
                if v[i]==0:
                    dfs(t,i,v)
                    t+=1
            
        for i in range(len(b)):
            adj[b[i][0]].append(b[i][1])
            adj[b[i][1]].append(b[i][0])
            v=[0]*n
            solve(v);f=0
            for j in range(len(a)):
                if v[a[j][0]]==v[a[j][1]]:
                    ans.append(False)
                    adj[b[i][0]].pop()
                    adj[b[i][1]].pop()
                    f=1
                    break
            if f==0:
                ans.append(True)
        return ans