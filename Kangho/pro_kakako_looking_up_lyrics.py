class Node:
    def __init__(self, data):
        self.data = data
        self.children = {}
        self.children_length = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head
        ls = len(string)
        if ls not in curr_node.children_length:
            curr_node.children_length[ls] = 1
        else:
            curr_node.children_length[ls] += 1
        for i, char in enumerate(string):
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
            if (ls-i-1) not in curr_node.children_length:
                curr_node.children_length[ls-i-1] = 1
            else:
                curr_node.children_length[ls-i-1] += 1

    def search(self, string):
        curr_node = self.head
        ls = len(string)
        for i, char in enumerate(string):
            if char == '?':
                ls -= i
                break
            else:
                if char not in curr_node.children:
                    return 0
                curr_node = curr_node.children[char]
        if ls in curr_node.children_length:
            cnt = curr_node.children_length[ls]
        else:
            cnt = 0
        return cnt


def solution(words, queries):
    answer = []
    t = Trie()
    revers_t = Trie()
    for word in words:
        t.insert(word)
        revers_t.insert(word[::-1])
    for query in queries:
        if query[0] == "?":
            answer.append(revers_t.search(query[::-1]))
        else:
            answer.append(t.search(query))
    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?", "?????"]))
