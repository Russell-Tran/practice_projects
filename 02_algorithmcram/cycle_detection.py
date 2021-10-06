# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Aka 'two pointers' solution
"""

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        slow = head
        
        while fast and slow:
            fast = fast.next
            if fast is slow:
                return True
            if fast:
                fast = fast.next
                if fast is slow:
                    return True
            slow = slow.next
            
            
        return False