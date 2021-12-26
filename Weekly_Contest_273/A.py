class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return str(int(str(num)[::-1]))[::-1]==str(num)