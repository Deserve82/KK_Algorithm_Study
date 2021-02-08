import sys


class Node:
    def __init__(self, data, is_last=False):
        self.data = data
        self.is_last = is_last
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, holes):
        curr_node = self.head
        stick = 0
        for hole in holes:
            if hole not in curr_node.children:
                curr_node.children[hole] = Node(hole)
                print('--' * stick + hole)
            curr_node = curr_node.children[hole]
            stick += 1
        curr_node.is_last = True


gulls = []
for _ in range(int(input())):
    gulls.append(sys.stdin.readline().rstrip().split()[1:])
gulls.sort()
t = Trie()
for gull in gulls:
    t.insert(gull)
