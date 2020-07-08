N=int(input())
Ai=list(map(int,input().split()))

ans=''

for i in range(1,N+1):
    a=Ai.index(i)+1
    ans+=(str(a)+' ')

print(ans)
