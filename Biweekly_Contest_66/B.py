import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000000+7;mod2=998244353
class Solution:
    def minimumBuckets(self, street: str) -> int:
        n=len(street)
        i=c=0
        while i<n:
            if street[i]=='H':
                if i+1<n and street[i+1]=='.':
                    i+=3
                    c+=1
                elif i-1>=0 and street[i-1]=='.':
                    i+=1
                    c+=1
                else:
                    return -1
            else:
                i+=1
        return c