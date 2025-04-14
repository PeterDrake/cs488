class Node:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root=None):
        self.root = root

    def __iter__(self):
        def depth_first(node):
            yield node.item
            if node.left:
                yield from depth_first(node.left)
            if node.right:
                yield from depth_first(node.right)
        return depth_first(self.root)

t = Tree(Node('a', Node('b'), Node('c', Node('d'), Node('e'))))

for item in t:
    print(item)
