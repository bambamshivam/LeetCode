from itertools import permutations
class Solution:
    def minimumSum(self, nums: int) -> int:
        m=math.inf
        a=list(permutations(str(nums)))
        for i in a:
            m=min(int(i[0]+i[1])+int(i[2]+i[3]),m)
        return m