class Solution:
    def countMaxOrSubsets(self,a) -> int:
        n=len(a)
        print(a)
        def solve(i,v):
            ans.append(v)
            if i>=n:
                return
            for j in range(i,n):
                k=v|a[j]
                solve(j+1,k)
        ans=[];solve(0,0);ans.pop(0)
        return ans.count(max(ans))
                
        