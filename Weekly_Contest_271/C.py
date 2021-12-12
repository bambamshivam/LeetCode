class Solution:
    def minimumRefill(self, p: list[int], a,b) -> int:
        n=len(p);i=0;j=n-1;a1=a;b1=b;ans=0
        while i<j:
            if a>=p[i]:
                a-=p[i]
            else:
                a=a1;a-=p[i];ans+=1
            if b>=p[j]:
                b-=p[j]
            else:
                b=b1;b-=p[j];ans+=1
            i+=1;j-=1
        if i==j:
            if a>=b:
                if a>=p[i]:
                    a-=p[i]
                else:
                    a=a1;a-=p[i];ans+=1
            else:
                if b>=p[i]:
                    b-=p[i]
                else:
                    b=b1;b-=p[i];ans+=1
        return ans