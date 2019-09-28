def mergesort(arr):
    #print(arr)
    if(len(arr)>1):
        mid=int(len(arr)/2)
        lefthalf=arr[:mid]
        righthalf=arr[mid:]
        mergesort(lefthalf)
        #print("lefthalf",lefthalf)
        mergesort(righthalf)
        #print("righthalf",righthalf)
        merge(arr,lefthalf,righthalf)
def merge(arr,lefthalf,righthalf):
    print("left",lefthalf)
    print("right",righthalf)
    sol=0
    sag=0
    tum=0
    while sol<len(lefthalf) and  sag<len(righthalf):
        if lefthalf[sol]<righthalf[sag]:
            arr[tum]=lefthalf[sol]
            sol+=1
        else:
            arr[tum]=righthalf[sag]
            sag+=1
        tum+=1
    while sol<len(lefthalf):
        arr[tum]=lefthalf[sol]
        sol+=1
        tum+=1
    while sag<len(righthalf):
        arr[tum]=righthalf[sag]
        sag+=1
        tum+=1
    print(arr)   
arr=[9,8,5,0,1,66,75,90]
mergesort(arr)