class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        p=[0]*(len(nums)*2+1);nums=nums+nums;c=nums.count(1)//2;ans=math.inf
        for i in range(len(nums)):
            p[i+1]=p[i]+nums[i]
        for i in range(len(nums)-c+1):
            ans=min(ans,c-p[i+c]+p[i])
        return ans