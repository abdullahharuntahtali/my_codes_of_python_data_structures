def matristoplama(a,b,c,i,j):
    if(len(a)-1==i and len(a[0])-1==j):
        c[i][j]=a[i][j]+b[i][j]
        return c
    elif len(a[0])-1 != j and len(a[0])-1 != i :
        c[i][j]=a[i][j]+b[i][j]
        return matristoplama(a,b,c,i,j+1)
    else :
        c[i][j]=a[i][j]+b[i][j]
        j=0
        return   matristoplama(a,b,c,i+1,j) 
a=[[1,2,3],[1,2,3]]
b=[[1,2,3],[1,2,3]]
c=a
print(matristoplama(a,b,c,0,0))

