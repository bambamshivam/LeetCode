class Solution:
    def getDistances(self, arr: list[int]) -> list[int]:
        d=defaultdict(list);d1={};ans=[]
        for i in range(len(arr)):
            d[arr[i]].append(i)
        for ke in d:
            l=d[ke];p=[l[0]];s=[0]*len(l);s[-1]=l[-1];b=[]
            if len(l)==1:
                d[ke][0]=0;continue
            for i in range(1,len(l)):p.append(p[-1]+l[i])
            for i in range(len(l)-2,-1,-1):s[i]=s[i+1]+l[i]
            for i in range(len(l)):
                b.append(abs((i+1)*l[i]-p[i])+abs(s[i]-l[i]*(len(l)-i)))
            d[ke]=b
        for i in range(len(arr)):
            k=d1.get(arr[i],0)
            ans.append(d[arr[i]][k])
            d1[arr[i]]=k+1
        return ans