def bubblesort(arr):
    for i in range(len(arr)-1,0,-1):      
        for j in range(i):
            if(arr[j]>arr[j+1]):
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    print(arr,"\n",len(arr))
x=[9,8,5,0,-10,95,20,12,13,14,18,16,17]
bubblesort(x)