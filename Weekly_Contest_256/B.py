class Solution:
    def kthLargestNumber(self, nums, k: int) -> str:
        nums.sort(key=lambda x:(len(x),x))
        return nums[len(nums)-k]
        