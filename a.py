def binary_search(list, end, x):
    start = 0
    counter = 0
    while start <= end:
        mid = int((start + end) / 2)
        counter += 1
        if list[mid] == x:
            return mid, counter
        elif list[mid] > x:
            end = mid - 1
        elif list[mid] < x:
            start = mid + 1
    return None
S= [x for x in range(30, 100000)]
print(binary_search(S, len(S) - 1, 33))