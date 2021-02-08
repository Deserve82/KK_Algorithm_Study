import sys
from collections import deque

input = sys.stdin.readline
class Node:
    def __init__(self, data, is_last=None):
        self.data = data
        self.is_last = is_last
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head
        for s in string:
            if s not in curr_node.children:
                curr_node.children[s] = Node(s)
            curr_node = curr_node.children[s]
        curr_node.is_last = string

    def start_with(self, prefix):
        curr_node = self.head
        results = []
        trie_strs = None

        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
                trie_strs = curr_node
            else:
                return None
        q = deque(trie_strs.children.values())
        while q:
            node = q.popleft()
            if node.is_last is not None:
                results.append(node.is_last)

            q += list(node.children.values())

        return results


for _ in range(int(input().rstrip())):
    N = int(input().rstrip())
    t = Trie()
    numbers = []
    for _ in range(N):
        number = input().rstrip()
        numbers.append(number)
        t.insert(number)
    f = True
    for number in numbers:
        if len(t.start_with(number)) >= 1:
            f = False
            break
    if f:
        print("YES")
    else:
        print("NO")
