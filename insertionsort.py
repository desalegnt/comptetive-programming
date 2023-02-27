def insertionSort1(n, arr):
    # Write your code here
    var = arr.pop()
    arr.append(arr[-1])
    s=0
    for i in range(n-2,-1,-1):
        if arr[i] > var:
            arr[i+1] = arr[i]
            print(' '.join(list(map(str, arr))))
        else:
            s = 1
            break
    if not s:
        i -= 1 
    arr.insert(i+1,var)
    del arr[i+2]
    print(' '.join(list(map(str, arr))))
