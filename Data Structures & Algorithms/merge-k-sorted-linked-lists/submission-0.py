# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merge_list = []

        for lst in lists:
                curr = lst
                while curr:
                    merge_list.append(curr.val)
                    curr = curr.next
        
        merge_list.sort()

        curr = dummy = ListNode()

        for val in merge_list:
            curr.next = ListNode(val)
            curr = curr.next
        
        return dummy.next
        