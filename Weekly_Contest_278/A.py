class Solution:
    def findFinalValue(self, nums: list[int], abc: int) -> int:
        s=set(nums)
        while abc in s:abc*=2
        return abc