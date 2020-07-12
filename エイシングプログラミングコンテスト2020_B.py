N=int(input())
ai=list(map(int,input().split()))

ai=ai[::2]

ans=0

for i in range(len(ai)):
    if ai[i] %2==1:
        ans+=1
print(ans)
