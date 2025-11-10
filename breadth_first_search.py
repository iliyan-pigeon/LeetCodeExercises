from collections import deque


def level_order_traversal(root):
    result = []
    queue = deque([root])

    while queue:
        new_line = []
        n = len(queue)

        for i in range(n):
            new_node = queue.popleft()
            new_line.append(new_node.val)

            if new_node.left is not None:
                queue.append(new_node.left)
            if new_node.right is not None:
                queue.append(new_node.right)
        result.append(new_line)

    return result