class Solution:
    def sumOfThree(self, num: int) -> list[int]:
        if (num-3)%3!=0:return []
        c=(num-3)//3
        return [c,c+1,c+2]