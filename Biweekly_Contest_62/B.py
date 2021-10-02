class Solution:
    def numOfPairs(self, nums, target: str) -> int:
        n=len(nums)
        c=0
        for i in range(n):
            for j in range(n):
                if i!=j and nums[i]+nums[j]==target:
                    c+=1
        return c
        