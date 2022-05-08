class Solution:
    def largestGoodInteger(self, num: str) -> str:
        num=str(num);ans=-1;n=len(num)
        for i in range(n-2):
            if num[i]==num[i+1]==num[i+2]:ans=max(int(num[i:i+3]),ans)
        return "" if ans==-1 else str(ans)[0]*3
            