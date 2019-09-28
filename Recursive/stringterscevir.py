def stringterscevir(string):
    if(len(string)==1):
        return string
    else:
        print("Stringin Yeni Hali = {} 0. elemanı = {}".format(string,string[0]))
        return stringterscevir(string[1:])+string[0]
    
print(stringterscevir("imam"))

""" stringterscevir(imam)
    stringterscevir(mam)+i
    stringterscevir(am)+m
    stringterscevir(m)+a
    Ardından return string yapınca string=m idi;
    m+a=ma
    stringterscevir(am)=ma+m=mam
    stringterscevir(mam)+i=mami
    
    """