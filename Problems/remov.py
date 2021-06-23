class Solution:
    def maximumRemovals(self, s: str, p: str, removable: list[int]) -> int:
        for i in range(len(removable)):
            k=removable[i]
            if k+1!=len(s):
                s=s[:k]+s[k+1:]
            else:
                s=s[:k]
            for j in range(i+1,len(removable)):
                if removable[j]>removable[i]:
                    removable[j]-=1
            l=[]
            t=0
            c=0
            for j in p:
                if s[t]!=j:
                    while t<len(s) and s[t]!=j:
                        t+=1
                    t+=1
                    c+=1
                else:
                    c+=1
                    t+=1
                if c<len(p) and t>=len(s):
                    return i


        return len(removable)

obj=Solution()
print(obj.maximumRemovals("abcab","abc",[0,1,2,3,4]))