def binary_search_recursive(dizi,deger):
    if(len(dizi)==0):
        return False
    else:
        mid=int(len(dizi)/2)
        #found case
        if(dizi[mid]==deger):
            return True
        else:
            #lower
            if(dizi[mid]>deger):
                return  binary_search_recursive(dizi[:mid],deger)
            #upper
            else:
                return binary_search_recursive(dizi[mid+1:],deger)
dizi=[1,2,3,5,6,8,9,11,13,15,16,17,19,25,29,34,36,38]
print(binary_search_recursive(dizi,38))