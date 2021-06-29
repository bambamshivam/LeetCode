import math

class Solution(object):
    def maxProductDifference(self, nums):
        nums.sort()
        print(nums[-1]*nums[-2] - nums[0]*nums[1])

obj=Solution()
obj.maxProductDifference([5,6,2,7,4])