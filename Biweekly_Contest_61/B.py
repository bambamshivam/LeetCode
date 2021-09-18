class Solution:
    def findOriginalArray(self, l):
        di={}
        n=len(l)
        for i in range(n):
            di[l[i]]=di.get(l[i],0)+1
        l.sort()
        ans=[]
        for i in range(n):
            if di.get(l[i],0)>0:
                if l[i]==0:
                    if di.get(0,0)>1:
                        ans.append(0)
                        di[0]-=2
                    else:
                        return []
                else:
                    if di.get(l[i]*2,0)>0:
                        ans.append(l[i])
                        di[l[i]]-=1
                        di[l[i]*2]-=1
        for ke in di:
            if di[ke]!=0:
                return []
        return ans