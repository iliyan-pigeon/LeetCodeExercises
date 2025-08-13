class Solution:
    def isSameTree(self, p, q):

        def check(p_node, q_node):
            r = True

            if not p_node and not q_node:
                return r
            elif not p_node:
                return False
            elif not q_node:
                return False

            if p_node.val != q_node.val:
                r = False
                return r

            if p_node.left and q_node.left:
                r = check(p_node.left, q_node.left)
                if r is False:
                    return r
            elif not p_node.left and not q_node.left:
                pass
            else:
                r = False
                return r

            if p_node.right and q_node.right:
                r = check(p_node.right, q_node.right)
                if r is False:
                    return r
            elif not p_node.right and not q_node.right:
                pass
            else:
                r = False
                return r

            return r

        result = check(p, q)
        return result
    