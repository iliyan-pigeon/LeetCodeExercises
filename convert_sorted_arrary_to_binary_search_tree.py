from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        mid = len(nums) // 2
        move_left = 1
        move_right = 1
        left_first = True
        right_first = True

        root = TreeNode(nums[mid])
        current_node = root

        while mid - move_left >= 0:
            if left_first:
                left_first = False
            else:
                current_node = current_node.left
            left_node = TreeNode(nums[mid-move_left])
            current_node.left = left_node
            left_node.right = current_node
            move_left += 1

        current_node = root

        while mid + move_right < len(nums):
            if right_first:
                right_first = False
            else:
                current_node = current_node.right
            right_node = TreeNode(nums[mid+move_right])
            current_node.right = right_node
            right_node.left = current_node
            move_right += 1

        return root
