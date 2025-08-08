class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.dummy = ListNode()

    def get(self, index: int) -> int:
        i = 0
        current = self.dummy.next

        while current:
            if i == index:
                return current.val
            i += 1
            current = current.next

        return -1

    def addAtHead(self, val: int) -> None:
        new_next = self.dummy.next
        self.dummy.next = ListNode(val)
        self.dummy.next.next = new_next

    def addAtTail(self, val: int) -> None:
        current = self.dummy

        while current:
            if current.next is None:
                current.next = ListNode(val)
                return
            current = current.next

    def addAtIndex(self, index: int, val: int) -> None:
        i = 0
        current = self.dummy

        while current:
            if i == index:
                new_next = current.next
                current.next = ListNode(val)
                current.next.next = new_next
                return

            i += 1
            current = current.next

    def deleteAtIndex(self, index: int) -> None:
        i = 0
        current = self.dummy

        while current:
            if i == index:
                if current.next:
                    current.next = current.next.next
                return

            i += 1
            current = current.next
