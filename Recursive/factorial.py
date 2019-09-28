def factorial(value):

    if(value==0):    
        return 1
    else:
       print("Değer = {} Değer-1 = {}".format(value,value-1))
       return value*factorial(value-1)
        
print(factorial(5))

"""if şartı sağlanana kadar  ;
5*(4)
4*(3)
3*(2)
2*(1)
1*(0)
Bunları hafızaya böylece kaydeder.Ardından ;
1*1 (1*(0) idi (0) if şartı idi 1 döndürdüğümüz için 1 yaptı)
2*(1)=2
3*(2)=6
4*(3)=24
5*(4)=120 yaptı.Stack mantığı ile çalışıyor.Sondan başlayarak işlemi yapıyor  """