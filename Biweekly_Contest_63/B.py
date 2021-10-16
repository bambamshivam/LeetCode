class Solution:
    def winnerOfGame(self, l) -> bool:
        n=len(l)
        def solve(ch):
            i=a=0
            while i<n:
                if l[i]!=ch:
                    i+=1
                    continue
                j=i+1
                while j<n and l[j]==l[i]:
                    j+=1
                if j-i>=3:
                    a+=j-i-2
                i=j
            return a
        a=solve('A');b=solve('B')
        if a>b:
            return True
        else:
            return False