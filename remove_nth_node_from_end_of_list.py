class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution 1
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        first = second = dummy

        for _ in range(n + 1):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next


# Solution 2
class Solution(object):
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes_count = 0
        dummy_node = ListNode(0)
        dummy_node.next = head
        current = dummy_node.next

        while current:
            current = current.next
            nodes_count += 1

        node_to_remove = nodes_count - n + 1
        current = dummy_node
        current_node = 0

        while True:

            if current_node == node_to_remove-1:
                current.next = current.next.next
                break

            current_node += 1
            current = current.next

        return dummy_node.next
