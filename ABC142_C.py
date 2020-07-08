N=int(input())
Ai=list(map(int,input().split()))

dic={}

for i in range(1,N+1):
    a=Ai.index(i)+1
    dic[i]=a

ans=''
for i in range(1,N+1):
    ans+=str(dic[i])+' '
print(ans)