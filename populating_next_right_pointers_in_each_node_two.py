class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return

        nodes = [root]

        def inner(n):
            new_nodes = []
            while n:
                if n:
                    current = n.pop(0)
                    if current.left:
                        new_nodes.append(current.left)
                    if current.right:
                        new_nodes.append(current.right)
                    if n:
                        current.next = n[0]
            return new_nodes

        while nodes:
            nodes.extend(inner(nodes))

        return root
    