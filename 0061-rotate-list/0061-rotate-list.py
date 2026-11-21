
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next or k == 0:
            return head

        # Find length and tail
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # Reduce unnecessary rotations
        k = k % length

        if k == 0:
            return head

        # Connect tail to head (make circular list)
        tail.next = head

        # Find the new tail
        steps = length - k - 1
        new_tail = head

        for _ in range(steps):
            new_tail = new_tail.next

        # Set new head and break the circle
        new_head = new_tail.next
        new_tail.next = None

        return new_head
