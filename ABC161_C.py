N,K=map(int,input().split())

if K>N or N==0:
    print(N)
    exit()

D1=N//K
D2=N//K+1

Ans=min (abs(D1*K-N),abs(D2*K-N))
print(Ans)