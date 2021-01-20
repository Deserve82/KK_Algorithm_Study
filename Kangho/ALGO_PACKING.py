def get_items(weight, item_idx):
    if weight > W:
        return -999999999
    if item_idx >= N:
        return 0

    if cache[weight][item_idx] != -1:
        return cache[weight][item_idx]
    cache[weight][item_idx] = get_items(weight, item_idx + 1)
    if W >= items[item_idx][0]:
        cache[weight][item_idx] = max(cache[weight][item_idx],
                                      items[item_idx][1] + get_items(weight + items[item_idx][0], item_idx + 1))
    return cache[weight][item_idx]


def reconstruct(capa, item):
    if item == N:
        return
    if capa > W:
        return
    if get_items(capa, item) == get_items(capa, item + 1):
        reconstruct(capa, item + 1)
    else:
        answer.append(items[item][2])
        reconstruct(capa + items[item][0], item + 1)


for _ in range(int(input())):
    N, W = map(int, input().split())
    cache = [[-1] * N for _ in range(W+1)]
    items = []
    answer = []
    for _ in range(N):
        name, w, d = input().split()
        items.append((int(w), int(d), name))
    reconstruct(0, 0)
    print(get_items(0, 0), len(answer))
    for a in answer:
        print(a)
