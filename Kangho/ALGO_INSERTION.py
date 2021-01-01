# 파이썬 del을 이용한 간단한 풀이
for _ in range(int(input())):
    N = int(input())
    shifted = list(map(int, input().split()))
    A = [0]*N
    candidates = [i for i in range(1, N+1)]
    for i in range(N-1, -1, -1):
        A[i] = (candidates[i-shifted[i]])
        del candidates[i-shifted[i]]
    print(" ".join(map(str, A)))

# treap을 구현해 이용한 
import random


class Node:
    def __init__(self, data):
        self.priority = random.randrange(0, 100)
        self.data = data
        self.size = 1
        self.left = None
        self.right = None

    def calc_size(self):
        self.size = 1
        if self.left:
            self.size += self.left.size
        if self.right:
            self.size += self.right.size

    def set_left(self, new_node):
        self.left = new_node
        self.calc_size()

    def set_right(self, new_node):
        self.right = new_node
        self.calc_size()


def split(root, data):
    if root is None:
        return None, None
    if root.data < data:
        rs = split(root.right, data)
        root.set_right(rs[0])
        return root, rs[1]
    ls = split(root.left, data)
    root.set_left(ls[0])
    return ls[0], root


def insert(root, node):
    if root is None:
        return node
    if root.priority < node.priority:
        splitted = split(root, node.data)
        node.set_left(splitted[0])
        node.set_right(splitted[1])
        return node
    elif node.data < root.data:
        root.set_left(insert(root.left, node))
    else:
        root.set_right(insert(root.right, node))
    return root


def merge(a, b):
    if a is None:
        return b
    if b is None:
        return a
    if a.priority < b.priority:
        b.set_left(merge(a, b.left))
        return b
    a.set_right(merge(a.right, b))
    return a


def erase(root, data):
    if root is None:
        return root
    if root.data == data:
        ret = merge(root.left, root.right)
        del root
        return ret
    if data < root.data:
        root.set_left(erase(root.left, data))
    else:
        root.set_right(erase(root.right, data))
    return root


def kth(root, k):
    left_size = 0
    if root.left is not None:
        left_size = root.left.size
    if k <= left_size:
        return kth(root.left, k)
    if k == left_size+1:
        return root
    return kth(root.right, k - left_size - 1)


def count_less_than(root, data):
    if root is None:
        return 0
    if root.data >= data:
        return count_less_than(root.left, data)
    ls = 0
    if root.left:
        ls = root.left.size
    return ls + 1 + count_less_than(root.right, data)


for _ in range(int(input())):
    N = int(input())
    shifted = list(map(int, input().split()))
    A = [0] * N
    cadi = None
    for i in range(N):
        cadi = insert(cadi, Node(i+1))
    for i in range(N-1, -1, -1):
        larger = shifted[i]
        k = kth(cadi, i+1-larger)
        A[i] = k.data
        cadi = erase(cadi, k.data)
    print(" ".join(map(str, A)))


