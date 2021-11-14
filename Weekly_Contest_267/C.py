class Solution:
    def decodeCiphertext(self, s: str, rows: int) -> str:
        col=len(s)//rows;k=0;l=[['' for j in range(col)] for i in range(rows)]
        for i in range(rows):
            for j in range(col):
                l[i][j]=s[k]
                k+=1
        i=0;j=0;p=""
        while j<col:
            k=j
            while i<rows and k<col:
                p+=l[i][k]
                i+=1;k+=1
            j+=1;i=0
        return p.rstrip()