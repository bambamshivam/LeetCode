class Solution:
    def findGCD(self, nums) -> int:
        return math.gcd(max(nums),min(nums))
        