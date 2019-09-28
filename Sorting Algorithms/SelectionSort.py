def selectionsort(arr):
    for i in range(0,len(arr)):
        key=i
        for j in range(i+1,len(arr)):
            if arr[key]>arr[j]:
                key=j
        arr[i],arr[key]=arr[key],arr[i]
    print(arr)



x=[3,5,7,0,2,9,-2,10]
selectionsort(x)