import sys
input = lambda: sys.stdin.readline().rstrip()

def merge_sort(arr, temp, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, temp, left, mid)
        merge_sort(arr, temp, mid + 1, right)
        merge(arr, temp, left, mid, right)

def merge(arr, temp, left, mid, right):
    global count, result, K, flag
    if flag:
        return

    i, j, k = left, mid + 1, left

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1
        count += 1
        if count == K:
            result = temp[k - 1]
            flag = True
            return

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
        count += 1
        if count == K:
            result = temp[k - 1]
            flag = True
            return

    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1
        count += 1
        if count == K:
            result = temp[k - 1]
            flag = True
            return

    for i in range(left, right + 1):
        arr[i] = temp[i]

N, K = map(int, input().split())
arr = list(map(int, input().split()))

temp = [0] * N
count = 0
result = -1
flag = False

merge_sort(arr, temp, 0, N - 1)

print(result)