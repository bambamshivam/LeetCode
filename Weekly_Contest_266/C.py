class Solution:
    def minimizedMaximum(self, n: int, l) -> int:
        def solve(m):
            c=0
            for i in range(len(l)):
                c+=l[i]//m + 1*(l[i]%m!=0)
            return c<=n
            
        l1=1;r=max(l)+1;ans=0
        while l1<r:
            m=(l1+r)//2
            if solve(m):
                ans=m
                r=m
            else:
                l1=m+1
        return ans