def multiply(a,b):
    if b==0:
        return 0
    else:
        
        return a+multiply(a,b-1)
    
x=multiply(2,3)
print(x)
"""multiply(2,3)
            2+ multiply(2,2)
                        2 + multiply(2,1)
                                     2 + multiply(2,0)

Alttan gidersek ;
2 + multiply(2,0)=2 + 0(multiply(2,0) b==0 ise return 0)=2
2 + multiply(2,1)=2+  2(multiply(2,1) yukaridaki işlemin sonucu=2 idi)=4
2 + multiply(2,2)=2+4


"""