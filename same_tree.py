class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        result = True
        p_front = p
        q_front = q
        p_back = p
        q_back = q

        while p_front and q_front and p_back and q_back:
            if p_front.val != q_front.val:
                result = False
                break
            elif p_back.val != q_back.val:
                result = False
                break

            p_front = p_front.right
            q_front = q_front.right
            p_back = p_back.left
            q_back = q_back.left

        return result
