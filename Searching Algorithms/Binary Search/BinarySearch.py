def binarysearch(dizi,value):
    """Sıralı Dizilerde Kullanılır"""
    first_index=0
    last_index=len(dizi)-1 #Pythonda diziler 0dan başlar.1den değil
    found=False
    while(first_index<=last_index and not found):
        middle_index=int((first_index+last_index)/2)
        if(value==dizi[middle_index]):
            found=True
        else:
            if(value<dizi[middle_index]):
                last_index=middle_index-1
                #lower half
                print("Değerin indexi middle_indexten küçük")
            else:
                #upper half
                first_index=middle_index+1
                print("Değerin indexi middle_indexten büyük")
    return (middle_index,found)
x=[1,5,9,12,15,17,19,21,26,30,54,90]
print(binarysearch(x,90))
                
