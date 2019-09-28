def isPalindrome(string):
    if(len(string)<2):
        return True
    else:
        return string[0]==string[-1] and isPalindrome(string[1:-1])
x="abaaba"
print(isPalindrome(x))

"""
string=abaaba
1. return string=baab
2. return string=aa
3. return string=   (boş)
3.return and True =True
2. return(Yani string[0]=a-string[-1]=a) and True =True
1. return(string[0]=b -string[-1]=b) and True=True


"""