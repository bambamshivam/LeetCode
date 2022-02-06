class Solution:
    def numberOfArrays(self, d: list[int], lower: int, upper: int) -> int:
        ma=0;mi=0;ans=0;c=0
        for i in d:
            c+=i
            if c>=0:ma=max(ma,c)
            if c<=0:mi=min(mi,c)
        for i in range(lower,upper+1):
            if i+ma<=upper and i+mi>=lower:ans+=1
        return ans