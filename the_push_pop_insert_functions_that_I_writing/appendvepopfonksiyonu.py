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


