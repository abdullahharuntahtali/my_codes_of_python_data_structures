def mergeSort(arr,l,r):
    if l < r:        
        m = int((l+(r))/2)        
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r- m 
    left = [0] * (n1)
    right = [0] * (n2) 
    for i in range(0 , n1):
        left[i] = arr[l + i]
    for j in range(0 , n2):
        right[j] = arr[m + 1 + j] 
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2 :
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1 
    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1 
    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1
    print(arr)
aa=[9,8,5,0,81,80,82,80]
mergeSort(aa,0,len(aa)-1)