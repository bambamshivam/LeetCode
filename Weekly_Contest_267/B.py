# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head) :
        p,prev=head,head;c=0
        while p:
            p=p.next
            c+=1
        n=math.floor((math.sqrt(1+8*c)-1)/2)
        p=head;t=1;count=0
        while p and t<=n:
            if t%2!=0:
                prev=p
                p=p.next
                count+=1
                if count==t*(t+1)//2:
                    t+=1
            else:
                cur=p;nex=cur.next;s=1
                while s<t:
                    nexx=nex.next
                    nex.next=cur
                    cur=nex
                    nex=nexx
                    s+=1
                prev.next=cur;prev=p
                p.next=nex
                p=nex;count=t*(t+1)//2
                t+=1
        if (c- n*(n+1)//2)%2==0 and (c- n*(n+1)//2)>0:
            cur=p;nex=cur.next
            while nex:
                nexx=nex.next
                nex.next=cur
                cur=nex
                nex=nexx
                print(cur.val)
            prev.next=cur;p.next=nex
        return head