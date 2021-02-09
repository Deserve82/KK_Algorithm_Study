import sys
from collections import deque

directions = ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1))
points = {1: 0, 2: 0, 3: 1, 4: 1, 5: 2, 6: 3, 7: 5, 8: 11}


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
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
        curr_node.is_last = string

    def search(self, string):
        curr_node = self.head
        for char in string:
            if char not in curr_node.children:
                return -1
            curr_node = curr_node.children[char]
        if curr_node.is_last == string:
            return 1
        return 0


def bfs(start_row, start_col):
    global total_points, longest_word, total_cnt
    q = deque()
    q.append(([(start_row, start_col)], board[start_row][start_col]))
    while q:
        loc, word = q.popleft()
        row, col = loc[-1]
        for dr, dc in directions:
            mr, mc = row + dr, col + dc
            if 0 <= mr < 4 and 0 <= mc < 4:
                if (mr, mc) not in loc:
                    new_word = word + board[mr][mc]
                    res = t.search(new_word)
                    if res == 1:
                        if new_word not in found_words:
                            found_words[new_word] = 1
                            total_cnt += 1
                            total_points += points[len(new_word)]
                            if len(new_word) > len(longest_word):
                                longest_word = new_word
                            elif len(new_word) == len(longest_word):
                                top = [new_word, longest_word]
                                top.sort()
                                longest_word = top[0]
                        q.append(([*loc, (mr, mc)], new_word))
                    elif res == 0:
                        q.append(([*loc, (mr, mc)], new_word))
                    else:
                        continue


N = int(input())
t = Trie()
for _ in range(N):
    t.insert(sys.stdin.readline().rstrip())
input()
M = int(input())
for z in range(M):
    longest_word = ''
    total_points = 0
    found_words = {}
    total_cnt = 0
    board = []
    for _ in range(4):
        board.append(list(sys.stdin.readline().rstrip()))
    for i in range(4):
        for j in range(4):
            is_this_in_list = t.search(board[i][j])
            if is_this_in_list == 0:
                bfs(i, j)
            elif is_this_in_list == 1:
                if board[i][j] not in found_words:
                    found_words[board[i][j]] = 1
                    total_cnt += 1
                    if 1 > len(longest_word):
                        longest_word = board[i][j]
                    elif 1 == len(longest_word):
                        top = [board[i][j], longest_word]
                        top.sort()
                        longest_word = top[0]
                bfs(i, j)
            else:
                continue
    if z != M - 1:
        input()
    print(total_points, longest_word, total_cnt)
