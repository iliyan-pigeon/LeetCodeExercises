class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution 1
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


# Solution 2
class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return None

        count = {}
        current = head
        while current:
            if current.val not in count:
                count[current.val] = 0
            count[current.val] += 1
            current = current.next

        dummy = ListNode(0)
        dummy.next = head
        prev, current = dummy, head

        while current:
            if count[current.val] > 1:
                prev.next = current.next
            else:
                prev = current
            current = current.next

        return dummy.next
