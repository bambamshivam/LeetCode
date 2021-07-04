class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        n=len(nums)
        for i in range(n):
            a.append(nums[nums[i]])
        return a