N=int(input())
a=list(map(int,input().split()))

l=sorted(a)

# N=10
# l=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


ans=0

for i in range(N):
    if i>=1 and l[i]==l[i-1]:
        continue
    else:
        t=l[i]
        for j in range(N-i):
            c=l[i+j]
            if abs(c-t)<=2:
                continue
            else:
                _ans=j
                if _ans>ans:
                    ans=_ans
                else:
                    pass
                break
print(ans)