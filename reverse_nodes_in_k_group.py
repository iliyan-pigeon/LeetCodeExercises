class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        dummy = ListNode()
        dummy.next = head
        prev = dummy

        nodes_amount = 0
        reversed_nodes = 0

        while prev.next is not None:
            nodes_amount += 1
            prev = prev.next

        current = prev.next
        reversed_nodes += k
        while reversed_nodes < nodes_amount:
            for _ in range(k-1):
                next_node = current.next
                current.next = next_node.next
                next_node.next = prev.next
                prev.next = next_node

                reversed_nodes += k

        return dummy.next
