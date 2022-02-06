class Solution:
    def minCostSetTime(self, s: int, m: int, p: int, t: int) -> int:
        if t//60==0:
            a=str(t%60)
            a1=a
        else:
            if t//60<=99:
                a=str(t//60)+'0'*(2-len(str(t%60)))+str(t%60)
            else:
                a=''
            if t%60<=39:
                p1='' if t//60==1 else str(t//60 -1)
                a1=p1+str(t%60 + 60)
            else:a1=''
        res=math.inf
        if len(a)>0:
            ans=0;s1=str(s)
            for i in range(len(a)):
                if a[i]!=s1:ans+=m
                ans+=p;s1=a[i]
            res=min(res,ans)
        if len(a1)>0:
            ans=0;s1=str(s)
            for i in range(len(a1)):
                if a1[i]!=s1:ans+=m
                ans+=p;s1=a1[i]
            res=min(res,ans)
        return res