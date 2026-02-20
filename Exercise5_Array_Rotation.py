def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def rotate_array(arr, k):
    n = len(arr)
    if n == 0:
        return

    k = k % n

    reverse(arr, 0, n - 1)
    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    rotate_array(arr, k)
    print(arr)
