# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head) -> int:
        h=head;l=[];ans=0
        while h:
            l.append(h.val);h=h.next
        for i in range(len(l)//2):
            ans=max(ans,l[i]+l[len(l)-i-1])
        return ans