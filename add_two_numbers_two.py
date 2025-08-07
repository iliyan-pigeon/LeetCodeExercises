from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution 1
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_string = ""
        l2_string = ""

        while l1:
            l1_string += str(l1.val)
            l1 = l1.next

        while l2:
            l2_string += str(l2.val)
            l2 = l2.next

        result = int(l1_string) + int(l2_string)

        dummy = ListNode()
        current = dummy

        for ch in str(result):
            node = ListNode(int(ch))
            current.next = node
            current = current.next

        return dummy.next


# Solution 2
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        reversed_l1 = self.reverse_nodes(l1)
        reversed_l2 = self.reverse_nodes(l2)
        carry = 0
        dummy = ListNode(-1)
        curr = dummy
        while reversed_l1 or reversed_l2 or carry:
            reversed_l1_val = reversed_l1.val if reversed_l1 else 0
            reversed_l2_val = reversed_l2.val if reversed_l2 else 0
            sums = reversed_l1_val + reversed_l2_val + carry
            val, carry = sums % 10, sums // 10
            to_add = ListNode(val)
            curr.next = to_add
            curr = curr.next
            reversed_l1 = reversed_l1.next if reversed_l1 else None
            reversed_l2 = reversed_l2.next if reversed_l2 else None
        return self.reverse_nodes(dummy.next)

    def reverse_nodes(self, head):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
