class Solution:
    def validArrangement(self, pairs):
        adj=defaultdict(list);din,dout=defaultdict(lambda:0),defaultdict(lambda:0)
        for i in pairs:
            adj[i[0]].append(i[1])
            din[i[1]]+=1
            dout[i[0]]+=1
        s=pairs[0][0]
        for i in dout:
            if dout[i]-din[i]==1:
                s=i;break
        res=[]
        def dfs(i):
            h=adj[i]
            while h:
                dfs(h.pop())
            res.append(i)
        dfs(s);res.reverse()
        ans=[]
        for i in range(len(res)-1):
            ans.append([res[i],res[i+1]])
        return ans