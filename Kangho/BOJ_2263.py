# 내 풀이
import sys

sys.setrecursionlimit(1000000)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def print_pre_order(node):
    arr = ''
    arr += str(node.data) + " "
    if node.left:
        arr += str(print_pre_order(node.left))
    if node.right:
        arr += str(print_pre_order(node.right))
    return arr


def pre_order(left, right):
    global post_order_idx

    if left > right:
        return

    node = Node(post_order[post_order_idx])
    post_order_idx -= 1

    if left == right:
        return node

    in_order_idx = pos[node.data]
    node.right = pre_order(in_order_idx + 1, right)
    node.left = pre_order(left, in_order_idx - 1)
    return node


n = int(sys.stdin.readline())
in_order = list(map(int, sys.stdin.readline().split()))
post_order = list(map(int, sys.stdin.readline().split()))
post_order_idx = n - 1
pos = [0] * (max(in_order) + 1)
for i, v in enumerate(in_order):
    pos[v] = i
ans = pre_order(0, n - 1)
print(print_pre_order(ans))

# 빠른 다른 사람들의 훌륭한 풀이

import sys

sys.setrecursionlimit(1000000)


def pre_order(in_left, in_right, post_left, post_right):
    if post_left > post_right:
        return
    if in_left > in_right:
        return

    root = post_order[post_right]
    print(root, end=" ")
    inorder_root = inposition[root]
    left_size = inorder_root - in_left

    pre_order(in_left, inorder_root - 1, post_left, post_left + left_size - 1)
    pre_order(inorder_root + 1, in_right, post_left + left_size, post_right - 1)


n = int(sys.stdin.readline())
in_order = list(map(int, sys.stdin.readline().split()))
post_order = list(map(int, sys.stdin.readline().split()))
inposition = [0] * (max(in_order) + 1)
for i, v in enumerate(in_order):
    inposition[v] = i
pre_order(0, n - 1, 0, n - 1)
