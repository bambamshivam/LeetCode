class Solution:
    def countEven(self, num: int) -> int:
        ans=0
        for i in range(1,num+1):
            a=list(str(i))
            for i in range(len(a)):a[i]=int(a[i])
            if sum(a)%2==0:ans+=1
        return ans