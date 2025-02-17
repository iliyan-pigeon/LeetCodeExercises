class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        if not head or k == 1:
            return head

        # Step 1: Count total nodes
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        current = head

        # Count nodes
        count = 0
        while current:
            count += 1
            current = current.next

        # Step 2: Reverse in groups of k
        while count >= k:
            prev = None
            current = prev_group_end.next
            next_node = None

            # Reverse k nodes
            for _ in range(k):
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node

            # Connect reversed part with previous group
            temp = prev_group_end.next  # This is the old head (now tail)
            prev_group_end.next = prev  # prev is now the new head
            temp.next = current  # Connect to the next part of the list
            prev_group_end = temp  # Move prev_group_end to the new tail

            count -= k  # Reduce remaining nodes count

        return dummy.next
