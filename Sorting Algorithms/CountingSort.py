def countingsort(arr,maxvalue):
    n=len(arr)
    m=maxvalue+1 #0ıda dahil edersek +1 yapmamız gerekir
    count=[0]*m #m = 5 ise [0,0,0,0,0](0,1,2,3,4 den 0 tane var anlamına geliyor)
    for i in arr :
        count[i]+=1
    a=0
    for i in range(m):
        for j in range(count[i]):
            arr[a]=i
            a+=1
    print(arr)


x=[1,1,3,4,3,5,6,6,7,8,8,8]
countingsort(x,8)
    
    
    
    