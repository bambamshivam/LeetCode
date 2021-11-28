class Solution:
    def getAverages(self, nums, k: int) :
        n=len(nums);a=[-1]*n
        d=[0]*(n+1)
        for i in range(n):
            d[i+1]+=d[i]+nums[i]
        for i in range(k,n-k):
            a[i]=(d[i+k+1]-d[i-k])//(2*k+1)
        return a