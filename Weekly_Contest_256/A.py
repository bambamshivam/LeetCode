class Solution:
    def minimumDifference(self, nums, k: int) -> int:
        m=math.inf
        n=len(nums)
        nums.sort()
        for i in range(0,n-k+1):
            m=min(m,nums[i+k-1]-nums[i])
        return m
        