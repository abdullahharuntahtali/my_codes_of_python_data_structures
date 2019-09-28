def append(dizi,y):
    i=len(dizi)
    i+=1
    x=[None]*i
    for j in range (0,len(dizi)):
        x[j]=dizi[j]
    x[i-1]=y
    dizi=x
    return x
def pop(dizi):
    i=len(dizi)-1
    x=[None]*i
    
    for i in range(0,len(dizi)-1):
        x[i]=dizi[i]
    return x
def insert(dizi,index,eleman):
       
    a=[None]*(len(dizi)+1)
    syc=1
    if index==0 :
        a[0]=eleman
        for i in dizi:
            a[syc]=i
            syc+=1
        return a
    else:
        for i in range(0,index):
            a[i]=dizi[i]
        a[index]=eleman
        syc=index
        for i in range(index+1,len(dizi)+1):
            a[i]=dizi[syc]
            syc+=1
        return a  
