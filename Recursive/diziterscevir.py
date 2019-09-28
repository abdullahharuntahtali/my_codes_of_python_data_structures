def diziterscevir(dizi):
    
    if (len(dizi)<2):
        return dizi
    else:
        temp=dizi[-1]
        dizi[-1]=dizi[0]
        dizi[0]=temp

        print(dizi)
        return dizi[0],diziterscevir(dizi[1:-1]),dizi[-1]
x=["a","t","a","r","i","c","i"]
print(diziterscevir(x))