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
def recursive_binary_search(list,start, end, x):
    counter =0

    if start <= end:
        mid = int((start + end)/2)
        counter +=1
        if list[mid] == x:
            return mid
        elif list[mid] > x:
            return recursive_binary_search(list,start, mid -1, x)
        elif list[mid] < x:
            return recursive_binary_search(list,mid + 1, end, x)
    else:
        return None
S= [x for x in range(30, 100000)]
print(recursive_binary_search(S,0, len(S) - 1, 33))