# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        nodes_count = 0
        curr = head
        
        while curr:
            nodes_count += 1
            if nodes_count == k:
                nxt = curr.next

                end, group_head = self.reverse_list(prev.next, k) 
                
                prev.next = group_head
                
                if head == prev.next.next: # Update head for the return value
                    head = group_head

                end.next = nxt
                curr = prev = end
                nodes_count = 0
            
            curr = curr.next

        return dummy.next

    
    def reverse_list(self, head: Optional[ListNode], k: int):
        end, prev = head, None

        while head and k:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
            k -= 1
        
        return (end, prev)