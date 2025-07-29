from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodesA = []
        nodesB = []

        while headA or headB:
            if headA:
                nodesA.append(headA)
            if headB:
                nodesB.append(headB)

            if headB in nodesA:
                return headB

            if headA in nodesB:
                return headA

            if headA:
                headA = headA.next
            if headB:
                headB = headB.next

        return