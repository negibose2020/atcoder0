N=int(input())
a=list(map(int,input().split()))

l=sorted(a)

ans=1

for i in range(N):
    t=l[i]
    _ans=0
    for j in range (N-i):
        c=l[i+j]
        if c-t<=2:
            pass
        else:
            _ans=j
            break
    if _ans>ans:
        ans=_ans
    else:
        pass
print(ans)
