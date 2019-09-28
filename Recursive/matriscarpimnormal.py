a=[]
b=[]
sonuc=[]
satira=int(input("a matrisinin satır uzunluğu = "))
sutuna=int(input("a matrisinin sütun uzunluğu = "))
satirb=int(input("b matrisinin satır uzunluğu = "))
sutunb=int(input("b matrisinin sütun uzunluğu = "))
if(sutuna!=satirb):
    print("Matrisler Çarpılamaz")
    exit();
for i in range(satira):
    a+=[[0]*sutuna]    
for i in range(satirb):
    b+=[[0]*sutunb]
for i in range(satira):
    sonuc+=[[0]*sutunb]
for i in range(satira):
    for j in range(sutuna):
        a[i][j]=int(input("{} satır {} sütundaki değeri girin . ".format(i,j)))
print("A Matrisi = ",a)
for i in range(satirb):
    for j in range(sutunb):
        b[i][j]=int(input("{} satır {} sütundaki değeri girin . ".format(i,j)))
print("B Matrisi = ",b)
for i in range(satira):
    for j in range(sutunb): 
        for k in range(satirb):#range(sutuna) da olurdu.
            sonuc[i][j]+=a[i][k]*b[k][j]            
print("\n\n\n",sonuc)