import sys


class Node:
    def __init__(self, data, is_last=None):
        self.data = data
        self.is_last = is_last
        self.freq = 1
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            else:
                curr_node.freq += 1
            curr_node = curr_node.children[char]
        curr_node.is_last = string

    def search(self, string):
        curr_node = self.head
        cnt = 1
        for char in string:
            curr_node = curr_node.children[char]
            if curr_node.is_last == string:
                return cnt
            if len(curr_node.children) > 1 or curr_node.is_last is not None:
                cnt += 1


while True:
    try:
        n = input()
    except EOFError:
        break
    n = int(n)
    t = Trie()
    words = []
    for _ in range(n):
        word = sys.stdin.readline().rstrip()
        words.append(word)
        t.insert(word)
    ts = 0
    for word in words:
        ts += t.search(word)
    print(format(round(ts/n, 2), ".2f"))
