def bi_search(l, r, arr, x):
    if r >= l:
        mid = (l+r)//2
        if arr[mid] == x:
            return 'Found'
        elif arr[mid] > x:
            return bi_search(l, mid-1, arr, x)
        elif arr[mid] < x:
            return bi_search(mid+1, r, arr, x)
    else:
        return 'Not found'


inp = input('Enter Input : ').split('/')

arr, k = list(map(int, inp[0].split())), int(inp[1])
# print(sorted(arr))
# print(k)
print(bi_search(0, len(arr) - 1, sorted(arr), k))