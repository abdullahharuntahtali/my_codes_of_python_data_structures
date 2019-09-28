def kacbasamak(sayi):
    if(sayi<9):
        return 1
    else:
        return 1+kacbasamak(sayi/10)
x=2565
print(kacbasamak(x))