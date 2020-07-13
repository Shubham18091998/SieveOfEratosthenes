def soe(n):
    prime=[True for i in range(n+1)]
    p=2
    while(p*p<=n):
        for i in range(p*2,n+1,p):
            if prime[i]:
                prime[i]=False
        p+=1
    prime[0]=False
    prime[1]=False
    for i in range(n+1):
        if prime[i]:
            print(i, end=' ')

if __name__=='__main__':
    n=int(input())
    ans=soe(n)
