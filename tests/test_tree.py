from rb_tree.tree import RBTree

def test_insert_and_search():
    tree = RBTree()
    values = [10, 20, 30, 15, 5]
    for val in values:
        tree.insert(val)
    for val in values:
        assert tree.search(val) is not None
    assert tree.search(999) is None

def test_deuplicate_insert():
    tree = RBTree()
    tree.insert(10)
    tree.insert(10)
    assert tree.root.val == 10
    assert tree.root.left.val is None
    assert tree.root.right.val is None

def test_root_is_black():
    tree = RBTree()
    tree.insert(10)
    assert tree.root.red == False

def test_children_are_nil_on_insert():
    tree = RBTree()
    tree.insert(10)
    assert tree.root.right == tree.nil
    assert tree.root.left == tree.nil

def test_rbtree_structure_simple():
    tree = RBTree()
    tree.insert(20)
    tree.insert(10)
    tree.insert(30)

    assert tree.root.val == 20
    assert tree.root.left.val == 10
    assert tree.root.right.val == 30

    assert tree.root.left.parent == tree.root
    assert tree.root.right.parent == tree.root

def is_red(node):
    return node is not None and node.red == True

def test_no_red_red_violation():
    tree = RBTree()
    vals = [10, 20, 30, 15, 25, 5]
    for v in vals:
        tree.insert(v)

    def check_no_red_red(node):
        if node == tree.nil:
            return
        if is_red(node):
            assert not is_red(node.left)
            assert not is_red(node.right)
        check_no_red_red(node.left)
        check_no_red_red(node.right)

    check_no_red_red(tree.root)

def print_rbtree(node, indent="", last=True):
    if node is not None:
        # Choose symbol based on whether this is a right or left child
        prefix = "└── " if last else "├── "
        # Print node with color indicator
        color = "R" if node.red == True else "B"
        if node.val is not None:
            print(indent + prefix + f"[{color}] {node.val.path}")

        # Recurse on children
        indent += "    " if last else "│   "
        children = [child for child in [node.left, node.right] if child is not None]
        for i, child in enumerate(children):
            print_rbtree(child, indent, i == len(children) - 1)
    else:
        print(indent + ("└── " if last else "├── ") + "[ ]")  # Empty leaf placeholder
