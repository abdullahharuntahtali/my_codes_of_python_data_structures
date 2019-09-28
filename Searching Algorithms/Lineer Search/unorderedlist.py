def lineer_search_unordered_list(liste,value):
    index=0
    found=False
    while(len(liste)>index and not found):
        if(liste[index]==value):
            found=True
        else:
            index+=1
    return (found,index)
x=[1,5,9,6,99,-8,100,0,5,1,6]
print(lineer_search_unordered_list(x,8))