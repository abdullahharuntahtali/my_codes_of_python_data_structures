def lineer_search_ordered_list(dizi,value) :
    """Aradığım sayı dan büyük yere gelince stop değişkeni ile çık"""
    index=0
    found=False
    stop=False
    while(len(dizi)>index and not found and not stop):
        if(dizi[index]==value):
            found=True
        else:
            if value<dizi[index]:
                stop=True
            else:
                index+=1
    return (found,index)

x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
print(lineer_search_ordered_list(x,-5))