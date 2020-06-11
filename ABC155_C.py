N=int(input())
Sarr1=[]
Sarr2=[]
for _ in range(N):
    s=input()
    if Sarr1.count(s)==0:
        Sarr1.append(s)
        Sarr2.append(0)
    else:
        i=Sarr1.index(s)
        Sarr2[i]+=1
ans=[]
m=max(Sarr2)

for i in range(len(Sarr2)):
    if Sarr2[i]==m:
        ans.append(Sarr1[i])
    else:
        pass
FA=sorted(ans)
for z in FA:
    print(z)