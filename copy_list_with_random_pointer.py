class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None

        # Step 1: Create cloned nodes and interleave them with the original nodes
        curr = head
        while curr:
            newNode = Node(curr.val)  # Clone the node
            newNode.next = curr.next  # Insert next to original
            curr.next = newNode
            curr = newNode.next  # Move to next original node

        # Step 2: Assign random pointers to cloned nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next  # Point cloned node's random to the correct    node
            curr = curr.next.next  # Move two steps forward

        # Step 3: Separate the cloned list from the original
        curr = head
        copy_head = head.next  # Start of copied list
        copy_curr = copy_head

        while curr:
            curr.next = curr.next.next  # Restore original list
            copy_curr.next = copy_curr.next.next if copy_curr.next else None  # Move copied list
            curr = curr.next
            copy_curr = copy_curr.next

        return copy_head  # Return the deep copied list
