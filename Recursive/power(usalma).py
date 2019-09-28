def multiply(a,b):
    if b==0:
        return 0
    else:
        
        return a+multiply(a,b-1)
    
x=multiply(2,3)
print(x)

def power(x,y):
    if y==0:
        return 1
    else :
        return multiply(x,power(x,y-1))
    
print(power(2,3))

"""
power(2,3)
multiply(2,power(2,2))
            multiply(2,power(2,1))
                        multiply(2,power(2,0))
                        b==0 return 1 yani
                        multiply(2,1)oldu
                        oda eşittir=2
                        power(2,1)=2
                        multiply(2,2)=4
                        power(2,2)=
                        multiply(2,4)=8
                         



"""






