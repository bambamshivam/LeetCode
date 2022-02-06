class Solution:
    def smallestNumber(self, num: int) -> int:
        if num>0:
            s=str(num);l=[]
            for i in s:
                if i!='0':l.append(i)
            l.sort()
            ans=l[0]+'0'*s.count('0')+''.join(l[1:])
            return int(ans)
        else:
            return -1*int(''.join(map(str,sorted(list(str(abs(num))),reverse=True))))