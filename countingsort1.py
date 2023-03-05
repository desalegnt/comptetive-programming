def countingSort(arr):
    # Write your code here
    result = [0]* 100
    for i in range(0,n):
        result[arr[i]] += 1
    return result
