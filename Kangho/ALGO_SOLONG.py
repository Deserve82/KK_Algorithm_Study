import sys
class Node:
    def __init__(self, data, whole_data, is_last=False):
        self.data = data
        self.whole_data = whole_data
        self.is_last = is_last
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None, 0)

    def insert(self, string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char, string)
            curr_node = curr_node.children[char]

        curr_node.is_last = True

    def search(self, string):
        curr_node = self.head
        cnt = 0
        for char in string:
            cnt += 1
            if char in curr_node.children:
                curr_node = curr_node.children[char]
                if curr_node.whole_data == string:
                    if curr_node.is_last and curr_node.data == string[-1]:
                        return min(len(string), cnt + 1)
                    else:
                        return cnt + 1
            else:
                return len(string)

        return cnt


for _ in range(int(sys.stdin.readline())):
    t = Trie()
    N, M = map(int, sys.stdin.readline().split())
    points = []
    for _ in range(N):
        S, p = sys.stdin.readline().split()
        points.append((int(p), S))
    points.sort(key=lambda x: x[1])
    points.sort(key=lambda x: x[0], reverse=True)
    for _, s in points:
        t.insert(s)
    words = list(sys.stdin.readline().rstrip().split())
    answer = 0
    for word in words:
        answer += t.search(word)
    print(answer + len(words) - 1)
