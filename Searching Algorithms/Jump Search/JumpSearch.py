import math
def jumpsearch(dizi,value):
    n=len(dizi)
    step=int(math.sqrt(n)) #Dizinin uzunluğunun karekökünü atlama adımım yaptım
    prev=0
    while(dizi[step]<value):
        prev=step
        
        step+=int(math.sqrt(n))
        if(step>=n): #Bu adım olmasa idi dizi boyutu taşabilirdi
            step-=int(math.sqrt(n))
            break
        if(prev>=n):
            return -1
    while(dizi[prev]<value):
        prev+=1
        if(prev==step):
            return -1
    if(dizi[prev]==value):
        return prev
    else:
        return -1
dizi=[1,3,5,7,8,9,10,12,15,14,17,19,20,90,95,100,105,108]
print(jumpsearch(dizi,5))