class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def post_order(self, node):
        s = []
        if node.left:
            s.extend(self.post_order(node.left))
        if node.right:
            s.extend(self.post_order(node.right))
        s.append(str(node.data))
        return s


def search(arr, start, end, value):
    for i in range(start, end + 1):
        if arr[i] == value:
            return i


def make_tree(in_strt, in_end):
    global pre_idx
    if in_strt > in_end:
        return
    t_node = Node(preorder[pre_idx])
    pre_idx += 1

    if in_strt == in_end:
        return t_node

    in_index = search(inorder, in_strt, in_end, t_node.data)
    t_node.left = make_tree(in_strt, in_index-1)
    t_node.right = make_tree(in_index+1, in_end)
    return t_node


for _ in range(int(input())):
    N = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    pre_idx = 0
    ans = make_tree(0, N-1)
    bt = BinaryTree()
    print(" ".join(bt.post_order(ans)))
