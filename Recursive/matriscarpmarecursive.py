def matriscarpim(a,b,c,i,j,k):
    if(len(a)-1==i and len(b[0])-1==j and len(b)-1==k):
        c[i][j]+=a[i][k]*b[k][j]
        return c
    elif len(a)>i and len(b[0])>j and len(b)>k:
        c[i][j]+=a[i][k]*b[k][j]
        return matriscarpim(a,b,c,i,j,k+1)
    elif len(a)>i and len(b[0])>j and len(b)<=k :
        k=0
        return matriscarpim(a,b,c,i,j+1,k)
    else:
        j=0
        k=0
        return matriscarpim(a,b,c,i+1,j,k)
    
a=[[3,2],[-1,4],[-2,1]]
b=[[2,1,-1],[3,2,1]]
c=[[0,0,0],[0,0,0],[0,0,0]]
# [[6, 7], [8, 6], [13, 11]]
print(matriscarpim(a,b,c,0,0,0))