N=int(input())
Ai=list(map(int,input().split()))

ans=[]

for i in range(1,N+1):
    a=Ai.index(i)+1
    ans.append(str(a))

print(' '.join(ans))
