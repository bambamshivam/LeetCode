class Solution:
    def maxScoreIndices(self, nums: list[int]) -> list[int]:
        n=len(nums);p=[0]*n;p[0]=nums[0];ans=[]
        for i in range(1,n):p[i]=p[i-1]+nums[i]
        m=max(sum(nums),n-sum(nums))
        for i in range(1,n):
            m=max(m,p[-1]+i-2*p[i-1])
        for i in range(1,n):
            if p[-1]+i-2*p[i-1]==m:ans.append(i)
        if sum(nums)==m:ans.append(0)
        if n-sum(nums)==m:ans.append(n)
        return sorted(ans)