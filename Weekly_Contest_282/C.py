class Solution:
    def minimumTime(self, time: list[int], t: int) -> int:
        l=0;r=min(time)*t;ans=0
        while l<=r:
            m=(l+r)//2;c=0
            for i in time:c+=(m//i)
            if c>=t:ans=m;r=m-1
            else:l=m+1
        return ans