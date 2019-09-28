syc=0
def addition(array,syc):
    #print(syc)
    if syc==0 :
        return 0
    else:
        print(array[syc-1])
        return array[syc-1]+addition(array,syc-1)
    
x=[1,2,2,2]
print(addition(x,len(x)))
    