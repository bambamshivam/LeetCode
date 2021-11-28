class Solution:
    def findAllPeople(self, n: int, m, f: int) :
        s={};s[0]=1;s[f]=1;m.sort(key=lambda x:x[-1])
        i=0;p=len(m)
        while i<p:
            j=i
            adj={};q=deque();d1=set();d2=set()
            while j<p and m[j][-1]==m[i][-1]:
                if (m[j][0],m[j][1]) not in d2:
                    g1=adj.get(m[j][0],[]);g2=adj.get(m[j][1],[])
                    g1.append(m[j][1])
                    g2.append(m[j][0])
                    adj[m[j][0]]=g1
                    adj[m[j][1]]=g2
                    if m[j][0] in s and m[j][0] not in d1:
                        q.append(m[j][0]);d1.add(m[j][0])
                    if m[j][1] in s and m[j][1] not in d1:
                        q.append(m[j][1]);d1.add(m[j][1])
                    d2.add((m[j][0],m[j][1]))
                j+=1
            while q:
                r=q.popleft()
                for k in adj[r]:
                    if k not in s:
                        s[k]=1
                        q.append(k)
            i=j
        return list(s.keys())