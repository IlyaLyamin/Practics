def binary_search(arr: list, k: int, t: str, s: int):
    if arr[int(len(arr)/2)] == k:
        return (s + int(len(arr)/2))
    if (arr[int(len(arr)/2)] > k and t == "1") or (arr[int(len(arr)/2)] < k and t == "-1"):
        arr = arr[:int(len(arr)/2)]
        s = 0
    else:
        s += int(len(arr)/2)
        arr = arr[int(len(arr)/2):]
    return binary_search(arr, k, t, s)


if __name__ == "__main__":
    arr = list(map(int, input().split(" ")))
    k = int(input())
    type_sort = input()
    s = 0
    print(binary_search(arr, k, type_sort, s))