class Solution: 
    def select(self, arr, i):
        # code here 
        for j in range(i,-1,-1):
            if arr[j] > arr[j + 1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
        return arr

        
    def selectionSort(self, arr,n):
        #code here
        for i in range(n-1):
            arr = self.select(arr,i)
        return arr
