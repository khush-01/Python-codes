def pow(a,b,k,m):
    def mult(p,x):
        return ((p[0]*x[0]-p[1]*x[1])%m, (p[0]*x[1]+p[1]*x[0])%m)
    
    x=(a,b)
    P=(1,0)
    while k:
        if k%2:
            P=mult(P,x)
        k//=2
        x=mult(x,x)
    return P
            
for _ in range(int(input())):
    a,b,k,m=map(int,input().split())
    c,d=pow(a,b,k,m)
    print (c,d)
