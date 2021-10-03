class Solution:
    def waysToPartition(self, nums, k: int) -> int:
        n=len(nums)
        dp=[0]*n
        dp[0]=nums[0]
        for i in range(1,n):
            dp[i]=dp[i-1]+nums[i]
        d1={};d2={}
        for i in range(n):
            d1[dp[i]]=d1.get(dp[i],0)+1
        s=dp[-1]
        m=p=0
        for i in range(n):
            t=s+(k-nums[i])
            if t%2==0:
                p=d1.get(t//2 - (k-nums[i]),0)
                if dp[-1]==t//2 - (k-nums[i]):
                    p-=1
                if k!=nums[i]:
                    p+=d2.get(t//2,0)
                m=max(m,p)
            d2[dp[i]]=d2.get(dp[i],0)+1
            d1[dp[i]]-=1
        if s%2==0:
            p=dp[:-1].count(s//2)
        return max(m,p)