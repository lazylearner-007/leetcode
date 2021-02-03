# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#using iteration

class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head
        
        while(curr):
            t = curr.next
            curr.next = prev
            prev = curr
            curr = t
            
        return prev
    
    
