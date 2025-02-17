class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        values = []
        current = head

        while current:
            values.append(current.val)
            current = current.next

        dummy = ListNode()
        dummy.next = head
        current = dummy

        while current.next:
            if values.count(current.next.val) >= 2:
                current.next = current.next.next
            current = current.next

        return dummy.next
