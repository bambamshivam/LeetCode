class Solution:
    def timeRequiredToBuy(self, t, k: int) -> int:
        q=deque();c=0
        for i in range(len(t)):
            q.append([t[i],i])
        while q:
            if q[0][0]!=0:
                c+=1
                if q[0][1]==k and q[0][0]==1:
                    break
                if q[0][0]>1:
                    q.append([q[0][0]-1,q[0][1]])
                q.popleft()
        return c