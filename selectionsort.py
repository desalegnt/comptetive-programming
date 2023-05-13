#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here
        p = i
        for j in range(i,len(arr)):
            if arr[j] < arr[p]:
                p = j
        arr[i],arr[p] = arr[p],arr[i]
        return arr
            
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n-1):
            arr = self.select(arr, i)
        return arr
