from math import comb,gcd,log
class Solution:
    def coutPairs(self, nums: list[int], k: int) -> int:
        l={};ans=c=0
        for i in nums:
            g=gcd(k,i)
            l[g]=l.get(g,0)+1
        for i in l:
            if (i*i)%k==0:c+=comb(l[i],2)
        for i in l:
            for j in l:
                if j!=i and (i*j)%k==0:ans+=l[i]*l[j]
        return ans//2 + c