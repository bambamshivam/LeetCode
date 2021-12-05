class Solution:
    def findEvenNumbers(self, d):
        d.sort();ans=set();l=[]
        for i in range(len(d)):
            for j in range(len(d)):
                for k in range(len(d)):
                    if d[i]!=0 and d[k]%2==0 and i!=j and j!=k and i!=k:
                        t=d[i]*100+d[j]*10+d[k]
                        if t not in ans:
                            l.append(t)
        return l