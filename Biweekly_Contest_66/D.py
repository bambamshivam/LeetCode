import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000000+7;mod2=998244353
class Solution:
    def countPyramids(self, g) -> int:
        n=len(g);m=len(g[0])
        g1=[[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                g1[i][j]=g[i][j]
        g1.reverse()
        def solve(g):
            c=0
            for i in range(n-2,-1,-1):
                for j in range(m):
                    if g[i][j]>0 and i+1<n and j-1>=0 and j+1<m and g[i+1][j-1]*g[i+1][j]*g[i+1][j+1]>0:
                        t=min(g[i+1][j-1],g[i+1][j],g[i+1][j+1])
                        c+=t
                        g[i][j]+=t
            return c
        return solve(g)+solve(g1)