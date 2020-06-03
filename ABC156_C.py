import numpy as np

def IsDistributionBiased_Smaller (sortedarr,P):
    _ndarr=np.array(sortedarr)
    smallarr=np.where(_ndarr<=P)
    if len(smallarr) > len (sortedarr)//2:
        return True
    else:
        return False

def WorkloadCalculation(arr,P):
    D=0
    for a in range(len(arr)):
        d=abs(arr[a]-P)
        D += d**2
    return D

N=int(input())
Xlist=[]
X=input().split()
for x in X:
    _x=int(x)
    Xlist.append(_x)

Xlist.sort()
P=(Xlist[0]+Xlist[-1])//2

workload=10000000
STOPflg=False
    
if IsDistributionBiased_Smaller(Xlist,P) ==True:
    while STOPflg==False:
        _wl=WorkloadCalculation(Xlist,P)
        if _wl < workload:
            workload=_wl
            P+=1
        else:
            print(workload)
            STOPflg=True
            exit()
else:
    while STOPflg==False:
        _wl=WorkloadCalculation(Xlist,P)
        if _wl < workload:
            workload=_wl
            P-=1
        else:
            print(workload)
            STOPflg=True
            exit()
print(workload)