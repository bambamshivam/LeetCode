import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000000+7;mod2=998244353
class Solution:
    def minCost(self, s, h, rowCosts, colCosts) -> int:
        c=0;p=-1;q=-1
        if s[0]<=h[0]:
            p=1
        if s[1]<=h[1]:
            q=1
        for i in range(s[0]+p,h[0]+p,p):
            c+=rowCosts[i]
        for i in range(s[1]+q,h[1]+q,q):
            c+=colCosts[i]
        return c