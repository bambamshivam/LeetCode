# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head):
        h=head;a=[];l=[]
        while h:a.append(h.val);h=h.next
        s=0
        for i in a:
            if i==0:l.append(s);s=0
            else:s+=i
        l.pop(0)
        if len(l)==0:return None
        h=ListNode();prev=h;ans=h
        for i in range(len(l)):
            h.val=l[i]
            if i!=len(l)-1:
                h1=ListNode()
                h.next=h1
                h=h.next
        return ans