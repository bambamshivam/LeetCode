class Solution:
    def getDescentPeriods(self, prices: list[int]) -> int:
        n=len(prices)
        i=0;c=0
        while i<n:
            j=i+1
            while j<n and prices[j]==prices[j-1]-1:
                j+=1
            c+=(j-i+1)*(j-i)//2;i=j
        return c