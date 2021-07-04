class Solution(object):
    def eliminateMaximum(self, dist, speed):
        """
        :type dist: List[int]
        :type speed: List[int]
        :rtype: int
        """
        a=[]
        n=len(dist)
        for i in range(n):
            a.append(1.0*dist[i]/speed[i])
        a.sort()
        print(a)
        t=0
        f=0
        for i in range(n):
            if t>=a[i]:
                return t
            else:
                t+=1
        if f==0:
            return t


obj=Solution()
print(obj.eliminateMaximum([3,2,4],[5,2,3]))

