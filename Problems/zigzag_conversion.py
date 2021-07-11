class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        n=len(s)
        r=numRows
        if r==1 or n==1:
            return s
        else:
            x=n//(2*r -2)
            t=x+(r-2)*x
            p=n%(2*r -2)
            if p>r:
                t+=(1+(p-r))
            else:
                t+=1
            dp=[[" " for i in range(t)] for j in range(r)]
            k=t
            for i in range(n):
                x=(i+1)//(2*r -2)
                t=x+ (r-2)*x
                p=(i+1)%(2*r -2)
                if p>r:
                    t+=(1+(p-r))
                    j=r-(p-r+1)
                else:
                    if p!=0:
                        j=p-1
                        t+=1
                    else:
                        j=1
                dp[j][t-1]=s[i]
            s1=""
            for i in range(r):
                for j in range(k):
                    if dp[i][j]!=" ":
                        s1+=dp[i][j]
            return s1
                    
                
        
obj=Solution()
print(obj.convert("PAYPALISHIRING",4))