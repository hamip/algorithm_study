# https://leetcode.com/problems/merge-two-sorted-lists/

# 21. Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
            
        # recursive call
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        
        return l1
        
        
