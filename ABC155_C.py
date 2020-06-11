from collections import Counter

N=int(input())
S=[]

for _ in range(N):
    s=input()
    S.append(s)

c=Counter(S)

max_s_list= [kv[0] for kv in c.items() if kv[1]==max(c.values())]

ans=sorted(max_s_list)
for a in ans:
    print(a)