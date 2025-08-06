from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Node:
    def __init__(self, val: int=0, prev: 'Node' = None, next: 'Node' = None, child: 'Node' = None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


# Solution 1
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = ListNode()
        current = dummy
        previous = None

        def add_nodes(node, new_dummy, new_current, new_previous):

            while node:

                if not new_dummy.next:
                    new_current.next = Node(node.val)
                    new_current = new_current.next
                else:
                    new_current.next = Node(node.val)
                    new_current.prev = new_previous
                    new_previous = new_current
                    new_current = new_current.next

                if node.child:
                    new_head, new_dummy, new_current, new_previous = add_nodes(node.child, new_dummy, new_current, new_previous)

                node = node.next

            return new_dummy.next, new_dummy, new_current, new_previous

        head, dummy, current, previous = add_nodes(head, dummy, current, previous)

        return head