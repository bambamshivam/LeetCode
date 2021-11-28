class Solution:
    def targetIndices(self, nums, target) :
        return [i for i in range(len(nums)) if sorted(nums)[i]==target]