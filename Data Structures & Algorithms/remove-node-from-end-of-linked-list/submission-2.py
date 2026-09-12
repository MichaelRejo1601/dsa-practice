class Solution:
    def removeNthFromEnd(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:

        sentinel = ListNode(next=head)

        length = 0
        node = head

        while node:
            length += 1
            node = node.next

        target = length - n
        node = sentinel

        for _ in range(target):
            node = node.next

        node.next = node.next.next

        return sentinel.next
