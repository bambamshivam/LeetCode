class Solution:
    def minSessions(self, tasks, sessionTime: int) -> int:
        s=sessionTime
        c=0
        nums=tasks
        while len(nums)>0:
            n=len(nums)
            dp=[[0 for i in range(s+1)] for j in range(n+1)]
            for i in range(1,n+1):
                for j in range(1,s+1):
                    if j<nums[i-1]:
                        dp[i][j]=dp[i-1][j]
                    else:
                        dp[i][j]=max(nums[i-1]+dp[i-1][j-nums[i-1]],dp[i-1][j])
            i,j=n,s
            di={}
            while i>=1 and j>=1:
                if dp[i-1][j-nums[i-1]]+nums[i-1]==dp[i][j]:
                    di[i-1]=1
                    j-=nums[i-1]
                i-=1
            l=[]
            for i in range(n):
                if di.get(i,0)==0:
                    l.append(nums[i])
            nums=l
            c+=1
        return c
            
            
        
                          