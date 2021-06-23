class Solution:
    def minDifference(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        l=nums
        q=queries
        n=len(l)
        a=[]
        ar=[[0 for j in range(101)] for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(101):
                if l[i-1]==j:
                    ar[i][j]=ar[i-1][j]+1
                else:
                    ar[i][j]=ar[i-1][j]

        for i in range(len(q)):
            a1=ar[q[i][0]]
            a2=ar[q[i][1]+1]
            a3=[0]*101
            a4=[]
            for j in range(101):
                a3[j]=a2[j]-a1[j]
                if a3[j]>0:
                    a4.append(j)
            if len(a4)==1:
                a.append(-1)
            else:
                m=10**9
                for k in range(len(a4)-1):
                    t=a4[k+1]-a4[k]
                    if t!=0 and t<m:
                        m=t
                if m==10**5:
                    m=-1
                a.append(m)
        return a

obj=Solution()
print(obj.minDifference([1,3,4,8],  [[0,1],[1,2],[2,3],[0,3]]))