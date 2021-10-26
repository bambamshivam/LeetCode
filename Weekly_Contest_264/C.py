class Solution:
    def countHighestScoreNodes(self, p) -> int:
        n=len(p)
        c=[[] for i in range(n)]
        for i in range(n):
            if p[i]!=-1:
                c[p[i]].append(i)
        
        def solve(r):
            if len(c[r])==0:
                b[r]=1
                return 1
            a=0
            for i in c[r]:
                a+=solve(i)
            b[r]=1+a
            return b[r]
        b=[0]*n
        solve(0);ans=[0]*n
        for i in range(n):
            if p[i]!=-1:
                if len(c[i])==2:
                    ans[i]=b[c[i][0]]*b[c[i][1]]*(n-b[c[i][0]]-b[c[i][1]]-1)
                elif len(c[i])==1:
                    ans[i]=b[c[i][0]]*(n-b[c[i][0]]-1)
                else:
                    ans[i]=n-1
            elif p[i]==-1:
                if len(c[i])==2:
                    ans[i]=b[c[i][0]]*b[c[i][1]]
                elif len(c[i])==1:
                    ans[i]=b[c[i][0]]
                else:
                    ans[i]=n-1
        return ans.count(max(ans))