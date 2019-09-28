def listmultiply(list):
    if len(list)==0:
        return 0
    else:
        return list[0]+listmultiply(list[1:])
    
x=[1,2,3]
print(listmultiply(x))
"""
1. return =1+listmultiply([2,3])
2. return =2+listmultiply([3])
3. return =3+listmultiply([])
4. return =0 (Çünkü len(list)= 0 ise 0 döndürdük)
Ardından ;
1. adım=3+0=3
2. adım=2+3=5
3. adım=1+5=6
Stack boşalmış oldu.


"""
