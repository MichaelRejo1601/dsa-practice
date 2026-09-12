# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# You are given two non-empty linked lists l1 and l2 where each represent a non-negative integer


# the digits are storted in reverse order least->greatest

# each node contains a single digit
# you may assume the two numbers do not contain any leading zero

# return sum of two numbers as a linked list

# add -> add -> add -> add -> add -> add -> add -> add
# head ->

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        sentinal = ListNode()
        current = sentinal
        carry_over = 0

        while l1 or l2:

            first_num = None
            second_num = None

            if l1 != None:
                first_num = l1.val
                l1 = l1.next
            else:
                first_num = 0
            
            if l2 != None:
                second_num = l2.val
                l2 = l2.next
            else:
                second_num = 0
            
            s = carry_over + first_num + second_num
            node = ListNode(val = (s % 10))
            carry_over = s // 10

            current.next = node
            current = current.next
        
        if carry_over > 0:
            current.next = ListNode(val=carry_over)
        
        return sentinal.next


        