import unittest


# 선택 정렬
def selection_sort(arr):
    """
    전체 인덱스를 순회 하면서 그 뒤에 있는 값이 가장 작은 것을 현재 인덱스와 교체 하는 정렬 알고리즘
    최악, 평균, 최선 시간 복잡도 = O(n^2), O(n^2), O(n^2)
    """
    size = len(arr)
    for i in range(size):
        min_val, min_idx = arr[i], i
        for j in range(i, size):
            if min_val >= arr[j]:
                min_val, min_idx = arr[j], j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# 삽입 정렬
def insertion_sort(arr):
    """
    현재 가르키고 있는 인덱스의 값이 들어갈 위치를 찾는 정렬 알고리즘
    최악, 평균, 최선 시간 복잡도 = O(n^2), O(n^2), O(n)
    """
    size = len(arr)
    for i in range(1, size):
        pivot_val, comp_idx = arr[i], i - 1
        while 0 <= comp_idx and arr[comp_idx] > pivot_val:
            arr[comp_idx + 1] = arr[comp_idx]
            comp_idx -= 1
        arr[comp_idx + 1] = pivot_val
    return arr


# 병합 정렬
def merge(left, right):
    ret = []
    left_idx, right_idx = 0, 0
    left_size, right_size = len(left), len(right)
    while left_idx < left_size and right_idx < right_size:
        if left[left_idx] < right[right_idx]:
            ret.append(left[left_idx])
            left_idx += 1
        else:
            ret.append(right[right_idx])
            right_idx += 1
    while left_idx < left_size:
        ret.append(left[left_idx])
        left_idx += 1
    while right_idx < right_size:
        ret.append(right[right_idx])
        right_idx += 1
    return ret


def merge_sort(arr):
    """
    merge_sort 메소드를 통해 다 잘게 나누어 주고 그것을 인덱스에 맞게 병합해 주는 방식
    최악, 평균, 최선 시간 복잡도 = O(nlogn), O(nlogn), O(nlogn)
    """
    size = len(arr)
    if size <= 1:
        return arr
    mid = size // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


# 퀵 소트
def quick_sort(arr):
    """
    퀵소트의 특징으로는 중간 피벗으로 잡은 곳을 기준으로 양옆을 바꾼다는 특징이 있다. 즉, 분할과 정렬을 동시에 진행한다.
    최악, 평균, 최선 시간 복잡도 = O(n^2), O(nlogn), O(nlogn)
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]
    less = []
    more = []
    equal = []
    for num in arr:
        if num < pivot:
            less.append(num)
        elif num > pivot:
            more.append(num)
        else:
            equal.append(num)
    return quick_sort(less) + equal + quick_sort(more)

def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and pivot <= arr[right]:
            right -= 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[start], arr[right] = arr[right], arr[start]
    return right


def quick_sort_without_cache(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot - 1)
        quick_sort(arr, pivot + 1, end)
    return arr



class TestSortingAlgorithm(unittest.TestCase):
    arr1 = [3, 2, 1, -1, 20, 3, 6, 7, 8, 12, 3]
    arr2 = [3, 2, 1, -1, 20, 3, 6, 7, 8, 12, 3]
    arr2.sort()

    def test_selection_sort(self):
        self.assertEqual(selection_sort(self.arr1), self.arr2)

    def test_insertion_sort(self):
        self.assertEqual(insertion_sort(self.arr1), self.arr2)

    def test_merge_sort(self):
        self.assertEqual(merge_sort(self.arr1), self.arr2)

    def test_quick_sort(self):
        self.assertEqual(quick_sort(self.arr1), self.arr2)
        
if __name__ == '__main__':
    unittest.main()
