class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        c=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if ((nums[i]==nums[j]) and ((i*j)%k==0)):
                    c+=1
        return c