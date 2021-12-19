class Solution:
    def kIncreasing(self, arr: list[int], k: int) -> int:
        def solve(a):
            sub=[]
            for i in a:
                if len(sub)==0 or sub[-1]<=i:
                    sub.append(i)
                else:
                    j=bisect_right(sub,i)
                    sub[j]=i
            return len(sub)
        ans=0
        for i in range(k):
            a=[]
            for j in range(i,len(arr),k):
                a.append(arr[j])
            ans+=len(a)-solve(a)
        return ans