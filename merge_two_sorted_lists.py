class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution 1
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        current_list = []
        dummy_head = ListNode(0)
        current = dummy_head

        while list1 or list2:
            if list1:
                current_list.append(list1.val)

            if list2:
                current_list.append(list2.val)

            if list1:
                list1 = list1.next
            if list2:
                list2 = list2.next

        current_list.sort()

        for number in current_list:
            current.next = ListNode(number)
            current = current.next

        return dummy_head.next


# Solution 2
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 if list1 else list2

        return dummy.next

