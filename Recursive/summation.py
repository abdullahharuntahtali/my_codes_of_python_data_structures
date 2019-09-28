def summation(value):
    """Recursive Toplama Yapar.value=3 ise ; (3+2+1+0=6)"""
    if(value==0):
        return 0
    else:
        print("Değer = {} Değer-1 = {}".format(value,value-1))
        return value+summation(value-1)

x=summation(3)
print(x)

"""if şartı sağlanana kadar  ;
5+(4)
4+(3)
3+(2)
2+(1)
1+(0)
Bunları hafızaya böylece kaydeder.Ardından ;
1+(0)=1 (1+(0) idi (0) if şartı idi 0 döndürdüğümüz için 0 yaptı)
2+(1)=3
3+(2)=6
4+(3)=10
5+(4)=15 yaptı.Stack mantığı ile çalışıyor.Sondan başlayarak işlemi yapıyor   """