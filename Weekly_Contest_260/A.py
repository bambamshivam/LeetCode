class Solution:
    def maximumDifference(self, nums) -> int:
        m=-1
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[j]>nums[i]:
                    m=max(m,nums[j]-nums[i])
        return m
        