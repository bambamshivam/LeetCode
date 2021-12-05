# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head):
        if not head.next: return None
        h=head;c=s=0
        while h:
            c+=1
            h=h.next
        h=head
        while s<c//2:
            prev=h
            h=h.next
            s+=1
        prev.next=h.next
        return head