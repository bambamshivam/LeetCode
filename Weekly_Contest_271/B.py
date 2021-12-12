class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:
        s=0;n=len(nums)
        for i in range(n):
            ma=nums[i];mi=nums[i]
            for j in range(i-1,-1,-1):
                ma=max(nums[j],ma)
                mi=min(nums[j],mi)
                s+=ma-mi
        return s