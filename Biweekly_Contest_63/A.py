class Solution:
    def minMovesToSeat(self, a,b) -> int:
        a.sort()
        b.sort()
        s=0
        for i in range(len(a)):
            s+=abs(a[i]-b[i])
        return s