class Solution:
    def removeNthFromEnd(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        # Use a sentinel so removing the head is handled
        # the same way as removing any other node.
        sentinel = ListNode(next=head)

        # First pass: find the length of the list.
        length = 0
        node = head

        while node:
            length += 1
            node = node.next

        # The nth node from the end is at index:
        # length - n
        target = length - n

        # Second pass: walk to the node immediately
        # before the target.
        node = sentinel

        for _ in range(target):
            node = node.next

        # Remove the target node.
        node.next = node.next.next

        return sentinel.next
