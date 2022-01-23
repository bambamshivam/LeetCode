class Solution:
    def countElements(self, nums: list[int]) -> int:
        nums.sort();c=0
        for i in range(1,len(nums)-1):
            if nums[0]<nums[i]<nums[-1]:c+=1
        return c