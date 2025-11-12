from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        new_nodes = {}

        def node_creation(the_node):
            if not the_node:
                return None

            new_node = Node(the_node.val)

            new_nodes[the_node.val] = new_node

            the_neighbors = []

            for n in the_node.neighbors:
                if n.val not in new_nodes:
                    current_neighbor = node_creation(n)
                else:
                    current_neighbor = new_nodes[n.val]

                the_neighbors.append(current_neighbor)

            new_node.neighbors = the_neighbors

            return new_node

        return node_creation(node)
    