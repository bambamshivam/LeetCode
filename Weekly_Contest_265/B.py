# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head) :
        a=[]
        while head:
            a.append(head.val)
            head=head.next
        n=len(a);j=-1;t=math.inf;k=-1
        for i in range(1,n-1):
            if a[i-1]<a[i]>a[i+1] or a[i-1]>a[i]<a[i+1]:
                if j!=-1:
                    t=min(t,i-j)
                j=i
                if k==-1:
                    k=i
        if t==math.inf:
            return [-1,-1]
        return [t,j-k]
                