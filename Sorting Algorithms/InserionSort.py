def insertionsort(arr):
    for i in range(1,len(arr)):
        currentvalue=arr[i]
        position=i
        while(position>0 and arr[position-1]>currentvalue):
            arr[position]=arr[position-1]
            position-=1
        arr[position]=currentvalue
    return arr


arr=[5,1,2,9,0,4,10,95,90]
print(insertionsort(arr))

