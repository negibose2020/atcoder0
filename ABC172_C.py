import bisect

N,M,K=map(int,input().split())
list_a=list(map(int,input().split()))
list_b=list(map(int,input().split()))


totaltame_a=[0]
for a in list_a:
    temp_a=totaltame_a[-1]+a
    if temp_a>K:
        break
    else:
        totaltame_a.append(temp_a)


totaltime_b=[0]
for b in list_b:
    totaltime_b.append(totaltime_b[-1]+b)

ans=0

for i in range (len(totaltame_a)):
    Kb=K-totaltame_a[i]
    j=bisect.bisect_right(totaltime_b,Kb)-1
    if i+j>ans:
        ans=i+j
    else:
        pass

print(ans)