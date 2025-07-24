class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry, digit = divmod(total, 10)

            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next



list1 = ListNode(2)
list1_1 = ListNode(4)
list1_2 = ListNode(3)
list1.next = list1_1
list1_1.next = list1_2

list2 = ListNode(5)
list2_1 = ListNode(6)
list2_2 = ListNode(4)
list2.next = list2_1
list2_1.next = list2_2


a = Solution()
print(a.addTwoNumbers(list1, list2))
