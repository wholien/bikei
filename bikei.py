
def zeromatrix(n):
    ### return n by n zero matrix### 
    out = []
    for i in range(0,n): 
        r = []
        for j in range(0,n): r.append(0)
        out.append(r)
    return out

def tm(M):
    ### tuple matrix### 
    out  = []
    for x in M: out.append(tuple(x))
    return tuple(out)



def lm(M):
    ### list matrix### 
    out = []
    for x in M: out.append(list(x))
    return list(out)


def bgenreduce(X):
    # reduce U,L with gen=gen relations in rlist
    U,L,rlist=X[0],X[1],X[2]
    dm=[]
    while rlist!=[]:
        x=rlist[0]
        rlist[0:1]=[]
        if x[0]<x[1]:
            i,j=x[0],x[1]
        if x[0]>x[1]:
            i,j=x[1],x[0]
        XP1,XP2=zeromatrix(len(U)-1),zeromatrix(len(U)-1)
        for a in range(1,j):
            for b in range(1,j):
                if U[a-1][b-1]<j:
                    XP1[a-1][b-1]=U[a-1][b-1]
                if U[a-1][b-1]==j:
                    XP1[a-1][b-1]=i
                if U[a-1][b-1]>j:
                    XP1[a-1][b-1]=U[a-1][b-1]-1
            for b in range(j+1,len(U)+1):
                if U[a-1][b-1]<j:
                    XP1[a-1][b-2]=U[a-1][b-1]
                if U[a-1][b-1]==j:
                    XP1[a-1][b-2]=i
                if U[a-1][b-1]>j:
                    XP1[a-1][b-2]=U[a-1][b-1]-1
        for a in range(j+1,len(U)+1):
            for b in range(1,j):
                if U[a-1][b-1]<j:
                    XP1[a-2][b-1]=U[a-1][b-1]
                if U[a-1][b-1]==j:
                    XP1[a-2][b-1]=i
                if U[a-1][b-1]>j:
                    XP1[a-2][b-1]=U[a-1][b-1]-1
            for b in range(j+1,len(U)+1):
                if U[a-1][b-1]<j:
                    XP1[a-2][b-2]=U[a-1][b-1]
                if U[a-1][b-1]==j:
                    XP1[a-2][b-2]=i
                if U[a-1][b-1]>j:
                    XP1[a-2][b-2]=U[a-1][b-1]-1
        for a in range(1,j):
            if XP1[a-1][i-1]==0 and U[a-1][j-1]!=0:
                if U[a-1][j-1]<j:
                    XP1[a-1][i-1]=U[a-1][j-1]
                if U[a-1][j-1]==j:
                    XP1[a-1][i-1]=i
                if U[a-1][j-1]>j:
                    XP1[a-1][i-1]=U[a-1][j-1]-1
            if U[a-1][i-1]!=0 and U[a-1][j-1]!=0:
                if U[a-1][i-1]<U[a-1][j-1]:
                    if [U[a-1][i-1],U[a-1][j-1]]!=[i,j] and [U[a-1][i-1],U[a-1][j-1]]!=[j,i] and not(tuple([U[a-1][i-1],U[a-1][j-1]]) in rlist):
                        rlist.append(tuple([XP1[a-1][i-1],U[a-1][j-1]]))
                if U[a-1][i-1]>U[a-1][j-1]:
                    if [U[a-1][i-1],U[a-1][j-1]]!=[i,j] and [U[a-1][i-1],U[a-1][j-1]]!=[j,i] and not(tuple([U[a-1][j-1],U[a-1][i-1]]) in rlist):
                        rlist.append(tuple([U[a-1][j-1],U[a-1][i-1]]))
            if XP1[i-1][a-1]==0 and U[j-1][a-1]!=0:
                if U[j-1][a-1]<j:
                    XP1[i-1][a-1]=U[j-1][a-1]
                if U[j-1][a-1]==j:
                    XP1[i-1][a-1]=i
                if U[j-1][a-1]>j:
                    XP1[i-1][a-1]=U[j-1][a-1]-1
            if U[i-1][a-1]!=0 and U[j-1][a-1]!=0:
                if U[i-1][a-1]<U[j-1][a-1]:
                    if [U[i-1][a-1],U[j-1][a-1]]!=[i,j] and [U[i-1][a-1],U[j-1][a-1]]!=[j,i] and not(tuple([U[i-1][a-1],U[j-1][a-1]]) in rlist):
                        rlist.append(tuple([U[i-1][a-1],U[j-1][a-1]]))
                if U[i-1][a-1]>U[j-1][a-1]:
                    if [U[i-1][a-1],U[j-1][a-1]]!=[i,j] and [U[i-1][a-1],U[j-1][a-1]]!=[j,i] and not(tuple([U[j-1][a-1],XP1[i-1][a-1]]) in rlist):
                        rlist.append(tuple([U[j-1][a-1],U[i-1][a-1]]))
        for a in range(j+1,len(U)+1):
            if XP1[a-2][i-1]==0 and U[a-1][j-1]!=0:
                if U[a-1][j-1]<j:
                    XP1[a-2][i-1]=U[a-1][j-1]
                if U[a-1][j-1]==j:
                    XP1[a-2][i-1]=i
                if U[a-1][j-1]>j:
                    XP1[a-2][i-1]=U[a-1][j-1]-1
            if U[a-1][i-1]!=0 and U[a-1][j-1]!=0:
                if U[a-1][i-1]<U[a-1][j-1]:
                    if [U[a-1][i-1],U[a-1][j-1]]!=[i,j] and [U[a-1][i-1],U[a-1][j-1]]!=[j,i] and not(tuple([U[a-1][i-1],U[a-1][j-1]]) in rlist):
                        rlist.append(tuple([U[a-1][i-1],U[a-1][j-1]]))
                if U[a-1][i-1]>U[a-1][j-1]:
                    if [U[a-1][i-1],U[a-1][j-1]]!=[i,j] and [U[a-1][i-1],U[a-1][j-1]]!=[j,i] and not(tuple([U[a-1][j-1],U[a-1][i-1]]) in rlist):
                        rlist.append(tuple([U[a-1][j-1],U[a-1][i-1]]))
            if XP1[i-1][a-2]==0 and U[j-1][a-1]!=0:
                if U[j-1][a-1]<j:
                    XP1[i-1][a-2]=U[j-1][a-1]
                if U[j-1][a-1]==j:
                    XP1[i-1][a-2]=i
                if U[j-1][a-1]>j:
                    XP1[i-1][a-2]=U[j-1][a-1]-1
            if U[i-1][a-1]!=0 and U[j-1][a-1]!=0:
                if U[i-1][a-1]<U[j-1][a-1]:
                    if [U[i-1][a-1],U[j-1][a-1]]!=[i,j] and [U[i-1][a-1],U[j-1][a-1]]!=[j,i] and not(tuple([U[i-1][a-1],U[j-1][a-1]]) in rlist):
                        rlist.append(tuple([U[i-1][a-1],U[j-1][a-1]]))
                if U[i-1][a-1]>U[j-1][a-1]:
                    if [U[i-1][a-1],U[j-1][a-1]]!=[i,j] and [U[i-1][a-1],U[j-1][a-1]]!=[j,i] and not(tuple([U[j-1][a-1],U[i-1][a-1]]) in rlist):
                        rlist.append(tuple([U[j-1][a-1],U[i-1][a-1]]))
        for a in range(1,j):
            for b in range(1,j):
                if L[a-1][b-1]<j:
                    XP2[a-1][b-1]=L[a-1][b-1]
                if L[a-1][b-1]==j:
                    XP2[a-1][b-1]=i
                if L[a-1][b-1]>j:
                    XP2[a-1][b-1]=L[a-1][b-1]-1
            for b in range(j+1,len(L)+1):
                if L[a-1][b-1]<j:
                    XP2[a-1][b-2]=L[a-1][b-1]
                if L[a-1][b-1]==j:
                    XP2[a-1][b-2]=i
                if L[a-1][b-1]>j:
                    XP2[a-1][b-2]=L[a-1][b-1]-1
        for a in range(j+1,len(L)+1):
            for b in range(1,j):
                if L[a-1][b-1]<j:
                    XP2[a-2][b-1]=L[a-1][b-1]
                if L[a-1][b-1]==j:
                    XP2[a-2][b-1]=i
                if L[a-1][b-1]>j:
                    XP2[a-2][b-1]=L[a-1][b-1]-1
            for b in range(j+1,len(L)+1):
                if L[a-1][b-1]<j:
                    XP2[a-2][b-2]=L[a-1][b-1]
                if L[a-1][b-1]==j:
                    XP2[a-2][b-2]=i
                if L[a-1][b-1]>j:
                    XP2[a-2][b-2]=L[a-1][b-1]-1
        for a in range(1,j):
            if XP2[a-1][i-1]==0 and L[a-1][j-1]!=0:
                if L[a-1][j-1]<j:
                    XP2[a-1][i-1]=L[a-1][j-1]
                if L[a-1][j-1]==j:
                    XP2[a-1][i-1]=i
                if L[a-1][j-1]>j:
                    XP2[a-1][i-1]=L[a-1][j-1]-1
            if L[a-1][i-1]!=0 and L[a-1][j-1]!=0:
                if L[a-1][i-1]<L[a-1][j-1]:
                    if [L[a-1][i-1],L[a-1][j-1]]!=[i,j] and [L[a-1][i-1],L[a-1][j-1]]!=[j,i] and not(tuple([L[a-1][i-1],L[a-1][j-1]]) in rlist):
                        rlist.append(tuple([XP2[a-1][i-1],L[a-1][j-1]]))
                if L[a-1][i-1]>L[a-1][j-1]:
                    if [L[a-1][i-1],L[a-1][j-1]]!=[i,j] and [L[a-1][i-1],L[a-1][j-1]]!=[j,i] and not(tuple([L[a-1][j-1],L[a-1][i-1]]) in rlist):
                        rlist.append(tuple([L[a-1][j-1],L[a-1][i-1]]))
            if XP2[i-1][a-1]==0 and L[j-1][a-1]!=0:
                if L[j-1][a-1]<j:
                    XP2[i-1][a-1]=L[j-1][a-1]
                if L[j-1][a-1]==j:
                    XP2[i-1][a-1]=i
                if L[j-1][a-1]>j:
                    XP2[i-1][a-1]=L[j-1][a-1]-1
            if L[i-1][a-1]!=0 and L[j-1][a-1]!=0:
                if L[i-1][a-1]<L[j-1][a-1]:
                    if [L[i-1][a-1],L[j-1][a-1]]!=[i,j] and [L[i-1][a-1],L[j-1][a-1]]!=[j,i] and not(tuple([L[i-1][a-1],L[j-1][a-1]]) in rlist):
                        rlist.append(tuple([L[i-1][a-1],L[j-1][a-1]]))
                if L[i-1][a-1]>L[j-1][a-1]:
                    if [L[i-1][a-1],L[j-1][a-1]]!=[i,j] and [L[i-1][a-1],L[j-1][a-1]]!=[j,i] and not(tuple([L[j-1][a-1],XP2[i-1][a-1]]) in rlist):
                        rlist.append(tuple([L[j-1][a-1],L[i-1][a-1]]))
        for a in range(j+1,len(L)+1):
            if XP2[a-2][i-1]==0 and L[a-1][j-1]!=0:
                if L[a-1][j-1]<j:
                    XP2[a-2][i-1]=L[a-1][j-1]
                if L[a-1][j-1]==j:
                    XP2[a-2][i-1]=i
                if L[a-1][j-1]>j:
                    XP2[a-2][i-1]=L[a-1][j-1]-1
            if L[a-1][i-1]!=0 and L[a-1][j-1]!=0:
                if L[a-1][i-1]<L[a-1][j-1]:
                    if [L[a-1][i-1],L[a-1][j-1]]!=[i,j] and [L[a-1][i-1],L[a-1][j-1]]!=[j,i] and not(tuple([L[a-1][i-1],L[a-1][j-1]]) in rlist):
                        rlist.append(tuple([L[a-1][i-1],L[a-1][j-1]]))
                if L[a-1][i-1]>L[a-1][j-1]:
                    if [L[a-1][i-1],L[a-1][j-1]]!=[i,j] and [L[a-1][i-1],L[a-1][j-1]]!=[j,i] and not(tuple([L[a-1][j-1],L[a-1][i-1]]) in rlist):
                        rlist.append(tuple([L[a-1][j-1],L[a-1][i-1]]))
            if XP2[i-1][a-2]==0 and L[j-1][a-1]!=0:
                if L[j-1][a-1]<j:
                    XP2[i-1][a-2]=L[j-1][a-1]
                if L[j-1][a-1]==j:
                    XP2[i-1][a-2]=i
                if L[j-1][a-1]>j:
                    XP2[i-1][a-2]=L[j-1][a-1]-1
            if L[i-1][a-1]!=0 and L[j-1][a-1]!=0:
                if L[i-1][a-1]<L[j-1][a-1]:
                    if [L[i-1][a-1],L[j-1][a-1]]!=[i,j] and [L[i-1][a-1],L[j-1][a-1]]!=[j,i] and not(tuple([L[i-1][a-1],L[j-1][a-1]]) in rlist):
                        rlist.append(tuple([L[i-1][a-1],L[j-1][a-1]]))
                if L[i-1][a-1]>L[j-1][a-1]:
                    if [L[i-1][a-1],L[j-1][a-1]]!=[i,j] and [L[i-1][a-1],L[j-1][a-1]]!=[j,i] and not(tuple([L[j-1][a-1],L[i-1][a-1]]) in rlist):
                        rlist.append(tuple([L[j-1][a-1],L[i-1][a-1]]))
        rlist2=[]
        for x in rlist:
            if x[0]<x[1]: y=x
            if x[0]>x[1]: y=tuple([x[1],x[0]]) # ensure y[0]<y[1]
            if y[0]>j: rlist2.append(tuple([y[0]-1,y[1]-1]))
            if y[0]==j: rlist2.append(tuple([i,y[1]-1]))
            if i<y[0] and y[0]<j:
                if y[1]>j: rlist2.append(tuple([y[0],y[1]-1]))
                if y[1]==j: rlist2.append(tuple([i,y[0]]))
                if y[1]<j: rlist2.append(tuple([y[0],y[1]]))
            if i==y[0]:
                if y[1]>j: rlist2.append(tuple([i,y[1]-1]))
                if y[1]<j: rlist2.append(tuple([i,y[1]]))
            if y[0]<i:
                if y[1]>j: rlist2.append(tuple([y[0],y[1]-1]))
                if y[1]==j: rlist2.append(tuple([y[0],i]))
                if y[1]<j: rlist2.append(tuple([y[0],y[1]]))
        U,L=lm(tm(XP1)),lm(tm(XP2))
        rlist=rlist2
    return [U,L]


def mybfill2(N):
    ### fill with yang-baxterity, involutority and mediality ###
    keepgoing = True
    rlist=[]
    U,L,n = lm(N[0]),lm(N[1]),len(N[0])
    while keepgoing:
        keepgoing = False
        for i in range(1,n+1):
            if U[i-1][i-1]!=0 and L[i-1][i-1]==0:
                L[i-1][i-1]=U[i-1][i-1]
                keepgoing=True
            if U[i-1][i-1]==0 and L[i-1][i-1]!=0:
                U[i-1][i-1]=L[i-1][i-1]
                keepgoing=True
            if U[i-1][i-1]!=0 and L[i-1][i-1]!=0:
                if L[i-1][i-1]>U[i-1][i-1] and not(tuple([U[i-1][i-1],L[i-1][i-1]]) in rlist):
                    rlist.append(tuple([U[i-1][i-1],L[i-1][i-1]]))
                if L[i-1][i-1]<U[i-1][i-1] and not(tuple([L[i-1][i-1],U[i-1][i-1]]) in rlist):
                    rlist.append(tuple([L[i-1][i-1],U[i-1][i-1]]))
            for j in range(1,n+1):
                if U[i-1][j-1]!=0:
                    if U[U[i-1][j-1]-1][j-1] == 0:
                        U[U[i-1][j-1]-1][j-1] = i
                        keepgoing = True
                    if U[U[i-1][j-1]-1][j-1] != i:
                        if U[U[i-1][j-1]-1][j-1] < i and not(tuple([U[U[i-1][j-1]-1][j-1],i]) in rlist):
                            rlist.append(tuple([U[U[i-1][j-1]-1][j-1],i]))
                        if U[U[i-1][j-1]-1][j-1] > i and not(tuple([i,U[U[i-1][j-1]-1][j-1]]) in rlist):
                            rlist.append(tuple([i,U[U[i-1][j-1]-1][j-1]]))
                if L[i-1][j-1]!=0:
                    if L[L[i-1][j-1]-1][j-1] == 0:
                        L[L[i-1][j-1]-1][j-1] = i
                        keepgoing = True
                    if L[L[i-1][j-1]-1][j-1] != i:
                        if L[L[i-1][j-1]-1][j-1] < i and not(tuple([L[L[i-1][j-1]-1][j-1],i]) in rlist):
                            rlist.append(tuple([L[L[i-1][j-1]-1][j-1],i]))
                        if L[L[i-1][j-1]-1][j-1] > i and not(tuple([i,L[L[i-1][j-1]-1][j-1]]) in rlist):
                            rlist.append(tuple([i,L[L[i-1][j-1]-1][j-1]]))
                if U[j-1][i-1]!=0 and L[i-1][j-1]!=0:
                    if U[U[j-1][i-1]-1][L[i-1][j-1]-1]==0:
                        U[U[j-1][i-1]-1][L[i-1][j-1]-1]=j
                        keepgoing=True
                    if U[U[j-1][i-1]-1][L[i-1][j-1]-1]!=j:
                        if j<U[U[j-1][i-1]-1][L[i-1][j-1]-1] and not(tuple([j,U[U[j-1][i-1]-1][L[i-1][j-1]-1]]) in rlist):
                            rlist.append(tuple([j,U[U[j-1][i-1]-1][L[i-1][j-1]-1]]))
                        if j>U[U[j-1][i-1]-1][L[i-1][j-1]-1] and not(tuple([U[U[j-1][i-1]-1][L[i-1][j-1]-1],j]) in rlist):
                            rlist.append(tuple([U[U[j-1][i-1]-1][L[i-1][j-1]-1],j]))
                    if L[L[i-1][j-1]-1][U[j-1][i-1]-1]==0:
                        L[L[i-1][j-1]-1][U[j-1][i-1]-1]=i
                        keepgoing=True
                    if L[L[i-1][j-1]-1][U[j-1][i-1]-1]!=i:
                        if i<L[L[i-1][j-1]-1][U[j-1][i-1]-1] and not(tuple([i,L[L[i-1][j-1]-1][U[j-1][i-1]-1]]) in rlist):
                            rlist.append(tuple([i,L[L[i-1][j-1]-1][U[j-1][i-1]-1]]))
                        if i>L[L[i-1][j-1]-1][U[j-1][i-1]-1] and not(tuple([L[L[i-1][j-1]-1][U[j-1][i-1]-1],i]) in rlist):
                            rlist.append(tuple([L[L[i-1][j-1]-1][U[j-1][i-1]-1],i]))
#                if U[i-1][j-1]==L[j-1][i-1]:
#                    if i<j and not(tuple([i,j]) in rlist):
#                        rlist.append(tuple([i,j]))
#                    if i>j and not(tuple([j,i]) in rlist):
#                        rlist.append(tuple([j,i]))
                if U[j-1][i-1]==i:
                    if L[i-1][j-1]==0:
                        L[i-1][j-1]=j
                        keepgoing=True
                    if L[i-1][j-1]!=j:
                        if L[i-1][j-1]<j and not(tuple([L[i-1][j-1],j]) in rlist):
                            rlist.append(tuple([L[i-1][j-1],j]))
                        if j<L[i-1][j-1] and not(tuple([j,L[i-1][j-1]]) in rlist):
                            rlist.append(tuple([j,L[i-1][j-1]]))
                if L[i-1][j-1]==j:
                    if U[j-1][i-1]==0:
                        U[j-1][i-1]=i
                        keepgoing=True
                    if U[j-1][i-1]!=i:
                        if U[j-1][i-1]<i and not(tuple([U[j-1][i-1],i]) in rlist):
                            rlist.append(tuple([U[j-1][i-1],i]))
                        if U[j-1][i-1]>i and not(tuple([i,U[j-1][i-1]]) in rlist):
                            rlist.append(tuple([i,U[j-1][i-1]]))
                if L[i-1][j-1]!=0:
                    if U[j-1][L[i-1][j-1]-1]==0 and U[j-1][i-1]!=0:
                        U[j-1][L[i-1][j-1]-1]=U[j-1][i-1]
                        keepgoing=True
                    if U[j-1][L[i-1][j-1]-1]!=0 and U[j-1][i-1]==0:
                        U[j-1][i-1]=U[j-1][L[i-1][j-1]-1]
                        keepgoing=True
                    if U[j-1][L[i-1][j-1]-1]!=U[j-1][i-1]:
                        if U[j-1][L[i-1][j-1]-1]<U[j-1][i-1] and not(tuple([U[j-1][L[i-1][j-1]-1],U[j-1][i-1]]) in rlist):
                            rlist.append(tuple([U[j-1][L[i-1][j-1]-1],U[j-1][i-1]]))
                        if U[j-1][L[i-1][j-1]-1]>U[j-1][i-1] and not(tuple([U[j-1][i-1],U[j-1][L[i-1][j-1]-1]]) in rlist):
                            rlist.append(tuple([U[j-1][i-1],U[j-1][L[i-1][j-1]-1]]))
                if U[j-1][i-1]!=0:
                    if L[i-1][U[j-1][i-1]-1]==0 and L[i-1][j-1]!=0:
                        L[i-1][U[j-1][i-1]-1]=L[i-1][j-1]
                        keepgoing=True
                    if L[i-1][U[j-1][i-1]-1]!=0 and L[i-1][j-1]==0:
                        L[i-1][j-1]=L[i-1][U[j-1][i-1]-1]
                        keepgoing=True
                    if L[i-1][U[j-1][i-1]-1]!=L[i-1][j-1]:
                        if L[i-1][U[j-1][i-1]-1]<L[i-1][j-1] and not(tuple([L[i-1][U[j-1][i-1]-1],L[i-1][j-1]]) in rlist):
                            rlist.append(tuple([L[i-1][U[j-1][i-1]-1],L[i-1][j-1]]))
                        if L[i-1][U[j-1][i-1]-1]>L[i-1][j-1] and not(tuple([L[i-1][j-1],L[i-1][U[j-1][i-1]-1]]) in rlist):
                            rlist.append(tuple([L[i-1][j-1],L[i-1][U[j-1][i-1]-1]]))
                for k in range(1,n+1):
                    if U[k-1][j-1]!=0 and L[i-1][j-1]!=0 and U[k-1][i-1]!=0 and U[j-1][i-1]!=0:
                        if U[U[k-1][j-1]-1][L[i-1][j-1]-1]==0 and U[U[k-1][i-1]-1][U[j-1][i-1]-1]!=0:
                            U[U[k-1][j-1]-1][L[i-1][j-1]-1]=U[U[k-1][i-1]-1][U[j-1][i-1]-1]
                            keepgoing=True
                        if U[U[k-1][j-1]-1][L[i-1][j-1]-1]!= 0 and U[U[k-1][i-1]-1][U[j-1][i-1]-1]==0:
                            U[U[k-1][i-1]-1][U[j-1][i-1]-1]=U[U[k-1][j-1]-1][L[i-1][j-1]-1]
                            keepgoing=True
                        if U[U[k-1][j-1]-1][L[i-1][j-1]-1]!=0 and U[U[k-1][i-1]-1][U[j-1][i-1]-1]!=0:
                            if U[U[k-1][j-1]-1][L[i-1][j-1]-1]<U[U[k-1][i-1]-1][U[j-1][i-1]-1] and not(tuple([U[U[k-1][j-1]-1][L[i-1][j-1]-1],U[U[k-1][i-1]-1][U[j-1][i-1]-1]])in rlist):
                                rlist.append(tuple([U[U[k-1][j-1]-1][L[i-1][j-1]-1],U[U[k-1][i-1]-1][U[j-1][i-1]-1]]))
                            if U[U[k-1][j-1]-1][L[i-1][j-1]-1]>U[U[k-1][i-1]-1][U[j-1][i-1]-1] and not(tuple([U[U[k-1][i-1]-1][U[j-1][i-1]-1],U[U[k-1][j-1]-1][L[i-1][j-1]-1]])in rlist):
                                rlist.append(tuple([U[U[k-1][i-1]-1][U[j-1][i-1]-1],U[U[k-1][j-1]-1][L[i-1][j-1]-1]]))
                    if U[j-1][i-1]!=0 and U[k-1][i-1]!=0 and L[j-1][k-1]!=0 and L[i-1][k-1]!=0:
                        if L[U[j-1][i-1]-1][U[k-1][i-1]-1]== 0 and U[L[j-1][k-1]-1][L[i-1][k-1]-1]!=0:
                            L[U[j-1][i-1]-1][U[k-1][i-1]-1]=U[L[j-1][k-1]-1][L[i-1][k-1]-1]
                            keepgoing=True
                        if L[U[j-1][i-1]-1][U[k-1][i-1]-1]!=0 and U[L[j-1][k-1]-1][L[i-1][k-1]-1]==0:
                            U[L[j-1][k-1]-1][L[i-1][k-1]-1]=L[U[j-1][i-1]-1][U[k-1][i-1]-1]
                            keepgoing=True
                        if L[U[j-1][i-1]-1][U[k-1][i-1]-1]!=U[L[j-1][k-1]-1][L[i-1][k-1]-1]:
                            if L[U[j-1][i-1]-1][U[k-1][i-1]-1]<U[L[j-1][k-1]-1][L[i-1][k-1]-1] and not(tuple([L[U[j-1][i-1]-1][U[k-1][i-1]-1],U[L[j-1][k-1]-1][L[i-1][k-1]-1]]) in rlist):
                                rlist.append(tuple([L[U[j-1][i-1]-1][U[k-1][i-1]-1],U[L[j-1][k-1]-1][L[i-1][k-1]-1]]))
                            if L[U[j-1][i-1]-1][U[k-1][i-1]-1]>U[L[j-1][k-1]-1][L[i-1][k-1]-1] and not(tuple([U[L[j-1][k-1]-1][L[i-1][k-1]-1],L[U[j-1][i-1]-1][U[k-1][i-1]-1]]) in rlist):
                                rlist.append(tuple([U[L[j-1][k-1]-1][L[i-1][k-1]-1],L[U[j-1][i-1]-1][U[k-1][i-1]-1]]))
                    if L[i-1][j-1]!=0 and U[k-1][j-1]!=0 and L[i-1][k-1]!=0 and L[j-1][k-1]!=0:
                        if L[L[i-1][j-1]-1][U[k-1][j-1]-1]==0 and L[L[i-1][k-1]-1][L[j-1][k-1]-1]!=0:
                            L[L[i-1][j-1]-1][U[k-1][j-1]-1]=L[L[i-1][k-1]-1][L[j-1][k-1]-1]
                            keepgoing=True
                        if L[L[i-1][j-1]-1][U[k-1][j-1]-1]!=0 and L[L[i-1][k-1]-1][L[j-1][k-1]-1]==0:
                            L[L[i-1][k-1]-1][L[j-1][k-1]-1]=L[L[i-1][j-1]-1][U[k-1][j-1]-1]
                            keepgoing=True
                        if L[L[i-1][j-1]-1][U[k-1][j-1]-1]!=L[L[i-1][k-1]-1][L[j-1][k-1]-1]:
                            if L[L[i-1][j-1]-1][U[k-1][j-1]-1]<L[L[i-1][k-1]-1][L[j-1][k-1]-1] and not(tuple([L[L[i-1][j-1]-1][U[k-1][j-1]-1],L[L[i-1][k-1]-1][L[j-1][k-1]-1]]) in rlist):
                                rlist.append(tuple([L[L[i-1][j-1]-1][U[k-1][j-1]-1],L[L[i-1][k-1]-1][L[j-1][k-1]-1]]))
                            if L[L[i-1][j-1]-1][U[k-1][j-1]-1]>L[L[i-1][k-1]-1][L[j-1][k-1]-1] and not(tuple([L[L[i-1][k-1]-1][L[j-1][k-1]-1],L[L[i-1][j-1]-1][U[k-1][j-1]-1]]) in rlist):
                                rlist.append(tuple([L[L[i-1][k-1]-1][L[j-1][k-1]-1],L[L[i-1][j-1]-1][U[k-1][j-1]-1]]))
                    if U[i-1][j-1] != 0 and L[k-1][j-1] != 0 and U[i-1][L[k-1][j-1]-1] !=0 and U[j-1][k-1] != 0:
                        if U[U[i-1][j-1]-1][k-1] != 0 and U[U[i-1][L[k-1][j-1]-1]-1][U[j-1][k-1]-1] == 0:
                            U[U[i-1][L[k-1][j-1]-1]-1][U[j-1][k-1]-1] = U[U[i-1][j-1]-1][k-1]
                            keepgoing = True
                        if U[U[i-1][j-1]-1][k-1] == 0 and U[U[i-1][L[k-1][j-1]-1]-1][U[j-1][k-1]-1] != 0:
                            U[U[i-1][j-1]-1][k-1] = U[U[i-1][L[k-1][j-1]-1]-1][U[j-1][k-1]-1] 
                            keepgoing = True
                        if U[U[i-1][j-1]-1][k-1] != U[U[i-1][L[k-1][j-1]-1]-1][U[j-1][k-1]-1]:
                            if U[U[i-1][j-1]-1][k-1]< U[U[i-1][L[k-1][j-1]-1]-1][U[j-1][k-1]-1] and not(tuple([U[U[i-1][j-1]-1][k-1],U[U[i-1][L[k-1][j-1]-1]-1][U[j-1][k-1]-1]]) in rlist):
                                rlist.append(tuple([U[U[i-1][j-1]-1][k-1],U[U[i-1][L[k-1][j-1]-1]-1][U[j-1][k-1]-1]]))
                            if U[U[i-1][j-1]-1][k-1]> U[U[i-1][L[k-1][j-1]-1]-1][U[j-1][k-1]-1] and not(tuple([U[U[i-1][L[k-1][j-1]-1]-1][U[j-1][k-1]-1],U[U[i-1][j-1]-1][k-1]]) in rlist):
                                rlist.append(tuple([U[U[i-1][L[k-1][j-1]-1]-1][U[j-1][k-1]-1],U[U[i-1][j-1]-1][k-1]]))
                    if L[j-1][i-1] != 0 and U[i-1][j-1] != 0 and L[k-1][U[i-1][j-1]-1] !=0 and U[j-1][k-1] != 0 and L[k-1][j-1] != 0 and U[i-1][L[k-1][j-1]-1] != 0:
                        if U[L[j-1][i-1]-1][L[k-1][U[i-1][j-1]-1]-1] != 0 and L[U[j-1][k-1]-1][U[i-1][L[k-1][j-1]-1]-1] == 0:
                            L[U[j-1][k-1]-1][U[i-1][L[k-1][j-1]-1]-1] = U[L[j-1][i-1]-1][L[k-1][U[i-1][j-1]-1]-1]
                            keepgoing = True
                        if U[L[j-1][i-1]-1][L[k-1][U[i-1][j-1]-1]-1] == 0 and L[U[j-1][k-1]-1][U[i-1][L[k-1][j-1]-1]-1] != 0:
                            U[L[j-1][i-1]-1][L[k-1][U[i-1][j-1]-1]-1] = L[U[j-1][k-1]-1][U[i-1][L[k-1][j-1]-1]-1]
                            keepgoing = True
                        if U[L[j-1][i-1]-1][L[k-1][U[i-1][j-1]-1]-1] != L[U[j-1][k-1]-1][U[i-1][L[k-1][j-1]-1]-1]:
                            if U[L[j-1][i-1]-1][L[k-1][U[i-1][j-1]-1]-1]< L[U[j-1][k-1]-1][U[i-1][L[k-1][j-1]-1]-1] and not(tuple([U[L[j-1][i-1]-1][L[k-1][U[i-1][j-1]-1]-1],L[U[j-1][k-1]-1][U[i-1][L[k-1][j-1]-1]-1]]) in rlist):
                                rlist.append(tuple([U[L[j-1][i-1]-1][L[k-1][U[i-1][j-1]-1]-1],L[U[j-1][k-1]-1][U[i-1][L[k-1][j-1]-1]-1]]))
                            if U[L[j-1][i-1]-1][L[k-1][U[i-1][j-1]-1]-1]> L[U[j-1][k-1]-1][U[i-1][L[k-1][j-1]-1]-1] and not(tuple([L[U[j-1][k-1]-1][U[i-1][L[k-1][j-1]-1]-1],U[L[j-1][i-1]-1][L[k-1][U[i-1][j-1]-1]-1]]) in rlist):
                                rlist.append(tuple([L[U[j-1][k-1]-1][U[i-1][L[k-1][j-1]-1]-1],U[L[j-1][i-1]-1][L[k-1][U[i-1][j-1]-1]-1]]))
                    if L[k-1][j-1] != 0 and L[j-1][i-1]!= 0 and U[i-1][j-1] != 0 and L[k-1][U[i-1][j-1]-1] != 0:
                        if L[L[k-1][j-1]-1][i-1] != 0 and L[L[k-1][U[i-1][j-1]-1]-1][L[j-1][i-1]-1] == 0:
                            L[L[k-1][U[i-1][j-1]-1]-1][L[j-1][i-1]-1] = L[L[k-1][j-1]-1][i-1]
                            keepgoing = True
                        if L[L[k-1][j-1]-1][i-1] == 0 and L[L[k-1][U[i-1][j-1]-1]-1][L[j-1][i-1]-1] != 0:
                            L[L[k-1][j-1]-1][i-1] = L[L[k-1][U[i-1][j-1]-1]-1][L[j-1][i-1]-1]
                            keepgoing = True
                        if L[L[k-1][j-1]-1][i-1] != L[L[k-1][U[i-1][j-1]-1]-1][L[j-1][i-1]-1]:
                            if L[L[k-1][j-1]-1][i-1] < L[L[k-1][U[i-1][j-1]-1]-1][L[j-1][i-1]-1] and not(tuple([L[L[k-1][j-1]-1][i-1],L[L[k-1][U[i-1][j-1]-1]-1][L[j-1][i-1]-1]]) in rlist):
                                rlist.append(tuple([L[L[k-1][j-1]-1][i-1],L[L[k-1][U[i-1][j-1]-1]-1][L[j-1][i-1]-1]]))
                            if L[L[k-1][j-1]-1][i-1] > L[L[k-1][U[i-1][j-1]-1]-1][L[j-1][i-1]-1] and not(tuple([L[L[k-1][U[i-1][j-1]-1]-1][L[j-1][i-1]-1],L[L[k-1][j-1]-1][i-1]]) in rlist):
                                rlist.append(tuple([L[L[k-1][U[i-1][j-1]-1]-1][L[j-1][i-1]-1],L[L[k-1][j-1]-1][i-1]]))
### Mediality
                    for l in range(1,len(U)+1):
                        if U[j-1][i-1]!=0 and U[k-1][l-1]!=0 and U[j-1][k-1]!=0 and U[i-1][l-1]!=0:
                            if U[U[j-1][i-1]-1][U[k-1][l-1]-1]!=0 and U[U[j-1][k-1]-1][U[i-1][l-1]-1]==0:
                                U[U[j-1][k-1]-1][U[i-1][l-1]-1]=U[U[j-1][i-1]-1][U[k-1][l-1]-1]
                                keepgoing=True
                            if U[U[j-1][i-1]-1][U[k-1][l-1]-1]==0 and U[U[j-1][k-1]-1][U[i-1][l-1]-1]!=0:
                                U[U[j-1][i-1]-1][U[k-1][l-1]-1]=U[U[j-1][k-1]-1][U[i-1][l-1]-1]
                                keepgoing=True
                            if U[U[j-1][i-1]-1][U[k-1][l-1]-1]!=U[U[j-1][k-1]-1][U[i-1][l-1]-1]:
                                if U[U[j-1][i-1]-1][U[k-1][l-1]-1]< U[U[j-1][k-1]-1][U[i-1][l-1]-1] and not(tuple([U[U[j-1][i-1]-1][U[k-1][l-1]-1],U[U[j-1][k-1]-1][U[i-1][l-1]-1]]) in rlist):
                                    rlist.append(tuple([U[U[j-1][i-1]-1][U[k-1][l-1]-1],U[U[j-1][k-1]-1][U[i-1][l-1]-1]]))
                                if U[U[j-1][i-1]-1][U[k-1][l-1]-1]>U[U[j-1][k-1]-1][U[i-1][l-1]-1] and not(tuple([U[U[j-1][k-1]-1][U[i-1][l-1]-1],U[U[j-1][i-1]-1][U[k-1][l-1]-1]]) in rlist):
                                    rlist.append(tuple([U[U[j-1][k-1]-1][U[i-1][l-1]-1],U[U[j-1][i-1]-1][U[k-1][l-1]-1]]))
                        if L[i-1][j-1]!=0 and L[k-1][l-1]!=0 and U[i-1][k-1]!=0 and U[j-1][l-1]!=0:
                            if U[L[i-1][j-1]-1][L[k-1][l-1]-1]==0 and L[U[i-1][k-1]-1][U[j-1][l-1]-1]!=0:
                                U[L[i-1][j-1]-1][L[k-1][l-1]-1]=L[U[i-1][k-1]-1][U[j-1][l-1]-1]
                                keepgoing=True
                            if U[L[i-1][j-1]-1][L[k-1][l-1]-1]!=0 and L[U[i-1][k-1]-1][U[j-1][l-1]-1]==0:
                                L[U[i-1][k-1]-1][U[j-1][l-1]-1]=U[L[i-1][j-1]-1][L[k-1][l-1]-1]
                                keepgoing=True
                            if U[L[i-1][j-1]-1][L[k-1][l-1]-1]!=L[U[i-1][k-1]-1][U[j-1][l-1]-1]:
                                if U[L[i-1][j-1]-1][L[k-1][l-1]-1]<L[U[i-1][k-1]-1][U[j-1][l-1]-1] and not(tuple([U[L[i-1][j-1]-1][L[k-1][l-1]-1],L[U[i-1][k-1]-1][U[j-1][l-1]-1]]) in rlist):
                                    rlist.append(tuple([U[L[i-1][j-1]-1][L[k-1][l-1]-1],L[U[i-1][k-1]-1][U[j-1][l-1]-1]]))
                                if U[L[i-1][j-1]-1][L[k-1][l-1]-1]>L[U[i-1][k-1]-1][U[j-1][l-1]-1] and not(tuple([L[U[i-1][k-1]-1][U[j-1][l-1]-1],U[L[i-1][j-1]-1][L[k-1][l-1]-1]]) in rlist):
                                    rlist.append(tuple([L[U[i-1][k-1]-1][U[j-1][l-1]-1],U[L[i-1][j-1]-1][L[k-1][l-1]-1]]))
                        if L[k-1][l-1]!=0 and L[i-1][j-1]!=0 and L[k-1][i-1]!=0 and L[l-1][j-1]!=0:
                            if L[L[k-1][l-1]-1][L[i-1][j-1]-1]==0 and L[L[k-1][i-1]-1][L[l-1][j-1]-1]!=0:
                                L[L[k-1][l-1]-1][L[i-1][j-1]-1]=L[L[k-1][i-1]-1][L[l-1][j-1]-1]
                                keepgoing=True
                            if L[L[k-1][l-1]-1][L[i-1][j-1]-1]!=0 and L[L[k-1][i-1]-1][L[l-1][j-1]-1]==0:
                                L[L[k-1][i-1]-1][L[l-1][j-1]-1]=L[L[k-1][l-1]-1][L[i-1][j-1]-1]
                                keepgoing=True
                            if L[L[k-1][l-1]-1][L[i-1][j-1]-1]!=L[L[k-1][i-1]-1][L[l-1][j-1]-1]:
                                if L[L[k-1][l-1]-1][L[i-1][j-1]-1]<L[L[k-1][i-1]-1][L[l-1][j-1]-1] and not(tuple([L[L[k-1][l-1]-1][L[i-1][j-1]-1],L[L[k-1][i-1]-1][L[l-1][j-1]-1]]) in rlist):
                                    rlist.append(tuple([L[L[k-1][l-1]-1][L[i-1][j-1]-1],L[L[k-1][i-1]-1][L[l-1][j-1]-1]]))
                                if L[L[k-1][l-1]-1][L[i-1][j-1]-1]>L[L[k-1][i-1]-1][L[l-1][j-1]-1] and not(tuple([L[L[k-1][i-1]-1][L[l-1][j-1]-1],L[L[k-1][l-1]-1][L[i-1][j-1]-1]]) in rlist):
                                    rlist.append(tuple([L[L[k-1][i-1]-1][L[l-1][j-1]-1],L[L[k-1][l-1]-1][L[i-1][j-1]-1]]))
#                    if (U[i-1][j-1] == U[k-1][j-1] and U[k-1][j-1]!=0) or (L[i-1][j-1] == L[k-1][j-1] and L[k-1][j-1]!=0):
#                        if i>k and not(tuple([k,i]) in rlist): 
#                            rlist.append(tuple([k,i]))
#                        if i<k and not(tuple([i,k]) in rlist):
#                            rlist.append(tuple([i,k]))
    return [U,L,rlist]




def ybfill2(N):
    ### fill with yang-baxterity and  involutority ###
    keepgoing = True
    rlist=[]
    U,L,n = lm(N[0]),lm(N[1]),len(N[0])
    while keepgoing:
        keepgoing = False
        for i in range(1,n+1):
            if U[i-1][i-1]!=0 and L[i-1][i-1]==0:
                L[i-1][i-1]=U[i-1][i-1]
                keepgoing=True
            if U[i-1][i-1]==0 and L[i-1][i-1]!=0:
                U[i-1][i-1]=L[i-1][i-1]
                keepgoing=True
            if U[i-1][i-1]!=0 and L[i-1][i-1]!=0:
                if L[i-1][i-1]>U[i-1][i-1] and not(tuple([U[i-1][i-1],L[i-1][i-1]]) in rlist):
                    rlist.append(tuple([U[i-1][i-1],L[i-1][i-1]]))
                if L[i-1][i-1]<U[i-1][i-1] and not(tuple([L[i-1][i-1],U[i-1][i-1]]) in rlist):
                    rlist.append(tuple([L[i-1][i-1],U[i-1][i-1]]))
            for j in range(1,n+1):
                if U[i-1][j-1]!=0:
                    if U[U[i-1][j-1]-1][j-1] == 0:
                        U[U[i-1][j-1]-1][j-1] = i
                        keepgoing = True
                    if U[U[i-1][j-1]-1][j-1] != i:
                        if U[U[i-1][j-1]-1][j-1] < i and not(tuple([U[U[i-1][j-1]-1][j-1],i]) in rlist):
                            rlist.append(tuple([U[U[i-1][j-1]-1][j-1],i]))
                        if U[U[i-1][j-1]-1][j-1] > i and not(tuple([i,U[U[i-1][j-1]-1][j-1]]) in rlist):
                            rlist.append(tuple([i,U[U[i-1][j-1]-1][j-1]]))
                if L[i-1][j-1]!=0:
                    if L[L[i-1][j-1]-1][j-1] == 0:
                        L[L[i-1][j-1]-1][j-1] = i
                        keepgoing = True
                    if L[L[i-1][j-1]-1][j-1] != i:
                        if L[L[i-1][j-1]-1][j-1] < i and not(tuple([L[L[i-1][j-1]-1][j-1],i]) in rlist):
                            rlist.append(tuple([L[L[i-1][j-1]-1][j-1],i]))
                        if L[L[i-1][j-1]-1][j-1] > i and not(tuple([i,L[L[i-1][j-1]-1][j-1]]) in rlist):
                            rlist.append(tuple([i,L[L[i-1][j-1]-1][j-1]]))
                if U[j-1][i-1]!=0 and L[i-1][j-1]!=0:
                    if U[U[j-1][i-1]-1][L[i-1][j-1]-1]==0:
                        U[U[j-1][i-1]-1][L[i-1][j-1]-1]=j
                        keepgoing=True
                    if U[U[j-1][i-1]-1][L[i-1][j-1]-1]!=j:
                        if j<U[U[j-1][i-1]-1][L[i-1][j-1]-1] and not(tuple([j,U[U[j-1][i-1]-1][L[i-1][j-1]-1]]) in rlist):
                            rlist.append(tuple([j,U[U[j-1][i-1]-1][L[i-1][j-1]-1]]))
                        if j>U[U[j-1][i-1]-1][L[i-1][j-1]-1] and not(tuple([U[U[j-1][i-1]-1][L[i-1][j-1]-1],j]) in rlist):
                            rlist.append(tuple([U[U[j-1][i-1]-1][L[i-1][j-1]-1],j]))
                    if L[L[i-1][j-1]-1][U[j-1][i-1]-1]==0:
                        L[L[i-1][j-1]-1][U[j-1][i-1]-1]=i
                        keepgoing=True
                    if L[L[i-1][j-1]-1][U[j-1][i-1]-1]!=i:
                        if i<L[L[i-1][j-1]-1][U[j-1][i-1]-1] and not(tuple([i,L[L[i-1][j-1]-1][U[j-1][i-1]-1]]) in rlist):
                            rlist.append(tuple([i,L[L[i-1][j-1]-1][U[j-1][i-1]-1]]))
                        if i>L[L[i-1][j-1]-1][U[j-1][i-1]-1] and not(tuple([L[L[i-1][j-1]-1][U[j-1][i-1]-1],i]) in rlist):
                            rlist.append(tuple([L[L[i-1][j-1]-1][U[j-1][i-1]-1],i]))
#                if U[i-1][j-1]==L[j-1][i-1]:
#                    if i<j and not(tuple([i,j]) in rlist):
#                        rlist.append(tuple([i,j]))
#                    if i>j and not(tuple([j,i]) in rlist):
#                        rlist.append(tuple([j,i]))
                if U[j-1][i-1]==i:
                    if L[i-1][j-1]==0:
                        L[i-1][j-1]=j
                        keepgoing=True
                    if L[i-1][j-1]!=j:
                        if L[i-1][j-1]<j and not(tuple([L[i-1][j-1],j]) in rlist):
                            rlist.append(tuple([L[i-1][j-1],j]))
                        if j<L[i-1][j-1] and not(tuple([j,L[i-1][j-1]]) in rlist):
                            rlist.append(tuple([j,L[i-1][j-1]]))
                if L[i-1][j-1]==j:
                    if U[j-1][i-1]==0:
                        U[j-1][i-1]=i
                        keepgoing=True
                    if U[j-1][i-1]!=i:
                        if U[j-1][i-1]<i and not(tuple([U[j-1][i-1],i]) in rlist):
                            rlist.append(tuple([U[j-1][i-1],i]))
                        if U[j-1][i-1]>i and not(tuple([i,U[j-1][i-1]]) in rlist):
                            rlist.append(tuple([i,U[j-1][i-1]]))
                if L[i-1][j-1]!=0:
                    if U[j-1][L[i-1][j-1]-1]==0 and U[j-1][i-1]!=0:
                        U[j-1][L[i-1][j-1]-1]=U[j-1][i-1]
                        keepgoing=True
                    if U[j-1][L[i-1][j-1]-1]!=0 and U[j-1][i-1]==0:
                        U[j-1][i-1]=U[j-1][L[i-1][j-1]-1]
                        keepgoing=True
                    if U[j-1][L[i-1][j-1]-1]!=U[j-1][i-1]:
                        if U[j-1][L[i-1][j-1]-1]<U[j-1][i-1] and not(tuple([U[j-1][L[i-1][j-1]-1],U[j-1][i-1]]) in rlist):
                            rlist.append(tuple([U[j-1][L[i-1][j-1]-1],U[j-1][i-1]]))
                        if U[j-1][L[i-1][j-1]-1]>U[j-1][i-1] and not(tuple([U[j-1][i-1],U[j-1][L[i-1][j-1]-1]]) in rlist):
                            rlist.append(tuple([U[j-1][i-1],U[j-1][L[i-1][j-1]-1]]))
                if U[j-1][i-1]!=0:
                    if L[i-1][U[j-1][i-1]-1]==0 and L[i-1][j-1]!=0:
                        L[i-1][U[j-1][i-1]-1]=L[i-1][j-1]
                        keepgoing=True
                    if L[i-1][U[j-1][i-1]-1]!=0 and L[i-1][j-1]==0:
                        L[i-1][j-1]=L[i-1][U[j-1][i-1]-1]
                        keepgoing=True
                    if L[i-1][U[j-1][i-1]-1]!=L[i-1][j-1]:
                        if L[i-1][U[j-1][i-1]-1]<L[i-1][j-1] and not(tuple([L[i-1][U[j-1][i-1]-1],L[i-1][j-1]]) in rlist):
                            rlist.append(tuple([L[i-1][U[j-1][i-1]-1],L[i-1][j-1]]))
                        if L[i-1][U[j-1][i-1]-1]>L[i-1][j-1] and not(tuple([L[i-1][j-1],L[i-1][U[j-1][i-1]-1]]) in rlist):
                            rlist.append(tuple([L[i-1][j-1],L[i-1][U[j-1][i-1]-1]]))
                for k in range(1,n+1):
                    if U[k-1][j-1]!=0 and L[i-1][j-1]!=0 and U[k-1][i-1]!=0 and U[j-1][i-1]!=0:
                        if U[U[k-1][j-1]-1][L[i-1][j-1]-1]==0 and U[U[k-1][i-1]-1][U[j-1][i-1]-1]!=0:
                            U[U[k-1][j-1]-1][L[i-1][j-1]-1]=U[U[k-1][i-1]-1][U[j-1][i-1]-1]
                            keepgoing=True
                        if U[U[k-1][j-1]-1][L[i-1][j-1]-1]!= 0 and U[U[k-1][i-1]-1][U[j-1][i-1]-1]==0:
                            U[U[k-1][i-1]-1][U[j-1][i-1]-1]=U[U[k-1][j-1]-1][L[i-1][j-1]-1]
                            keepgoing=True
                        if U[U[k-1][j-1]-1][L[i-1][j-1]-1]!=0 and U[U[k-1][i-1]-1][U[j-1][i-1]-1]!=0:
                            if U[U[k-1][j-1]-1][L[i-1][j-1]-1]<U[U[k-1][i-1]-1][U[j-1][i-1]-1] and not(tuple([U[U[k-1][j-1]-1][L[i-1][j-1]-1],U[U[k-1][i-1]-1][U[j-1][i-1]-1]])in rlist):
                                rlist.append(tuple([U[U[k-1][j-1]-1][L[i-1][j-1]-1],U[U[k-1][i-1]-1][U[j-1][i-1]-1]]))
                            if U[U[k-1][j-1]-1][L[i-1][j-1]-1]>U[U[k-1][i-1]-1][U[j-1][i-1]-1] and not(tuple([U[U[k-1][i-1]-1][U[j-1][i-1]-1],U[U[k-1][j-1]-1][L[i-1][j-1]-1]])in rlist):
                                rlist.append(tuple([U[U[k-1][i-1]-1][U[j-1][i-1]-1],U[U[k-1][j-1]-1][L[i-1][j-1]-1]]))
                    if U[j-1][i-1]!=0 and U[k-1][i-1]!=0 and L[j-1][k-1]!=0 and L[i-1][k-1]!=0:
                        if L[U[j-1][i-1]-1][U[k-1][i-1]-1]== 0 and U[L[j-1][k-1]-1][L[i-1][k-1]-1]!=0:
                            L[U[j-1][i-1]-1][U[k-1][i-1]-1]=U[L[j-1][k-1]-1][L[i-1][k-1]-1]
                            keepgoing=True
                        if L[U[j-1][i-1]-1][U[k-1][i-1]-1]!=0 and U[L[j-1][k-1]-1][L[i-1][k-1]-1]==0:
                            U[L[j-1][k-1]-1][L[i-1][k-1]-1]=L[U[j-1][i-1]-1][U[k-1][i-1]-1]
                            keepgoing=True
                        if L[U[j-1][i-1]-1][U[k-1][i-1]-1]!=U[L[j-1][k-1]-1][L[i-1][k-1]-1]:
                            if L[U[j-1][i-1]-1][U[k-1][i-1]-1]<U[L[j-1][k-1]-1][L[i-1][k-1]-1] and not(tuple([L[U[j-1][i-1]-1][U[k-1][i-1]-1],U[L[j-1][k-1]-1][L[i-1][k-1]-1]]) in rlist):
                                rlist.append(tuple([L[U[j-1][i-1]-1][U[k-1][i-1]-1],U[L[j-1][k-1]-1][L[i-1][k-1]-1]]))
                            if L[U[j-1][i-1]-1][U[k-1][i-1]-1]>U[L[j-1][k-1]-1][L[i-1][k-1]-1] and not(tuple([U[L[j-1][k-1]-1][L[i-1][k-1]-1],L[U[j-1][i-1]-1][U[k-1][i-1]-1]]) in rlist):
                                rlist.append(tuple([U[L[j-1][k-1]-1][L[i-1][k-1]-1],L[U[j-1][i-1]-1][U[k-1][i-1]-1]]))
                    if L[i-1][j-1]!=0 and U[k-1][j-1]!=0 and L[i-1][k-1]!=0 and L[j-1][k-1]!=0:
                        if L[L[i-1][j-1]-1][U[k-1][j-1]-1]==0 and L[L[i-1][k-1]-1][L[j-1][k-1]-1]!=0:
                            L[L[i-1][j-1]-1][U[k-1][j-1]-1]=L[L[i-1][k-1]-1][L[j-1][k-1]-1]
                            keepgoing=True
                        if L[L[i-1][j-1]-1][U[k-1][j-1]-1]!=0 and L[L[i-1][k-1]-1][L[j-1][k-1]-1]==0:
                            L[L[i-1][k-1]-1][L[j-1][k-1]-1]=L[L[i-1][j-1]-1][U[k-1][j-1]-1]
                            keepgoing=True
                        if L[L[i-1][j-1]-1][U[k-1][j-1]-1]!=L[L[i-1][k-1]-1][L[j-1][k-1]-1]:
                            if L[L[i-1][j-1]-1][U[k-1][j-1]-1]<L[L[i-1][k-1]-1][L[j-1][k-1]-1] and not(tuple([L[L[i-1][j-1]-1][U[k-1][j-1]-1],L[L[i-1][k-1]-1][L[j-1][k-1]-1]]) in rlist):
                                rlist.append(tuple([L[L[i-1][j-1]-1][U[k-1][j-1]-1],L[L[i-1][k-1]-1][L[j-1][k-1]-1]]))
                            if L[L[i-1][j-1]-1][U[k-1][j-1]-1]>L[L[i-1][k-1]-1][L[j-1][k-1]-1] and not(tuple([L[L[i-1][k-1]-1][L[j-1][k-1]-1],L[L[i-1][j-1]-1][U[k-1][j-1]-1]]) in rlist):
                                rlist.append(tuple([L[L[i-1][k-1]-1][L[j-1][k-1]-1],L[L[i-1][j-1]-1][U[k-1][j-1]-1]]))
                    if U[i-1][j-1] != 0 and L[k-1][j-1] != 0 and U[i-1][L[k-1][j-1]-1] !=0 and U[j-1][k-1] != 0:
                        if U[U[i-1][j-1]-1][k-1] != 0 and U[U[i-1][L[k-1][j-1]-1]-1][U[j-1][k-1]-1] == 0:
                            U[U[i-1][L[k-1][j-1]-1]-1][U[j-1][k-1]-1] = U[U[i-1][j-1]-1][k-1]
                            keepgoing = True
                        if U[U[i-1][j-1]-1][k-1] == 0 and U[U[i-1][L[k-1][j-1]-1]-1][U[j-1][k-1]-1] != 0:
                            U[U[i-1][j-1]-1][k-1] = U[U[i-1][L[k-1][j-1]-1]-1][U[j-1][k-1]-1] 
                            keepgoing = True
                        if U[U[i-1][j-1]-1][k-1] != U[U[i-1][L[k-1][j-1]-1]-1][U[j-1][k-1]-1]:
                            if U[U[i-1][j-1]-1][k-1]< U[U[i-1][L[k-1][j-1]-1]-1][U[j-1][k-1]-1] and not(tuple([U[U[i-1][j-1]-1][k-1],U[U[i-1][L[k-1][j-1]-1]-1][U[j-1][k-1]-1]]) in rlist):
                                rlist.append(tuple([U[U[i-1][j-1]-1][k-1],U[U[i-1][L[k-1][j-1]-1]-1][U[j-1][k-1]-1]]))
                            if U[U[i-1][j-1]-1][k-1]> U[U[i-1][L[k-1][j-1]-1]-1][U[j-1][k-1]-1] and not(tuple([U[U[i-1][L[k-1][j-1]-1]-1][U[j-1][k-1]-1],U[U[i-1][j-1]-1][k-1]]) in rlist):
                                rlist.append(tuple([U[U[i-1][L[k-1][j-1]-1]-1][U[j-1][k-1]-1],U[U[i-1][j-1]-1][k-1]]))
                    if L[j-1][i-1] != 0 and U[i-1][j-1] != 0 and L[k-1][U[i-1][j-1]-1] !=0 and U[j-1][k-1] != 0 and L[k-1][j-1] != 0 and U[i-1][L[k-1][j-1]-1] != 0:
                        if U[L[j-1][i-1]-1][L[k-1][U[i-1][j-1]-1]-1] != 0 and L[U[j-1][k-1]-1][U[i-1][L[k-1][j-1]-1]-1] == 0:
                            L[U[j-1][k-1]-1][U[i-1][L[k-1][j-1]-1]-1] = U[L[j-1][i-1]-1][L[k-1][U[i-1][j-1]-1]-1]
                            keepgoing = True
                        if U[L[j-1][i-1]-1][L[k-1][U[i-1][j-1]-1]-1] == 0 and L[U[j-1][k-1]-1][U[i-1][L[k-1][j-1]-1]-1] != 0:
                            U[L[j-1][i-1]-1][L[k-1][U[i-1][j-1]-1]-1] = L[U[j-1][k-1]-1][U[i-1][L[k-1][j-1]-1]-1]
                            keepgoing = True
                        if U[L[j-1][i-1]-1][L[k-1][U[i-1][j-1]-1]-1] != L[U[j-1][k-1]-1][U[i-1][L[k-1][j-1]-1]-1]:
                            if U[L[j-1][i-1]-1][L[k-1][U[i-1][j-1]-1]-1]< L[U[j-1][k-1]-1][U[i-1][L[k-1][j-1]-1]-1] and not(tuple([U[L[j-1][i-1]-1][L[k-1][U[i-1][j-1]-1]-1],L[U[j-1][k-1]-1][U[i-1][L[k-1][j-1]-1]-1]]) in rlist):
                                rlist.append(tuple([U[L[j-1][i-1]-1][L[k-1][U[i-1][j-1]-1]-1],L[U[j-1][k-1]-1][U[i-1][L[k-1][j-1]-1]-1]]))
                            if U[L[j-1][i-1]-1][L[k-1][U[i-1][j-1]-1]-1]> L[U[j-1][k-1]-1][U[i-1][L[k-1][j-1]-1]-1] and not(tuple([L[U[j-1][k-1]-1][U[i-1][L[k-1][j-1]-1]-1],U[L[j-1][i-1]-1][L[k-1][U[i-1][j-1]-1]-1]]) in rlist):
                                rlist.append(tuple([L[U[j-1][k-1]-1][U[i-1][L[k-1][j-1]-1]-1],U[L[j-1][i-1]-1][L[k-1][U[i-1][j-1]-1]-1]]))
                    if L[k-1][j-1] != 0 and L[j-1][i-1]!= 0 and U[i-1][j-1] != 0 and L[k-1][U[i-1][j-1]-1] != 0:
                        if L[L[k-1][j-1]-1][i-1] != 0 and L[L[k-1][U[i-1][j-1]-1]-1][L[j-1][i-1]-1] == 0:
                            L[L[k-1][U[i-1][j-1]-1]-1][L[j-1][i-1]-1] = L[L[k-1][j-1]-1][i-1]
                            keepgoing = True
                        if L[L[k-1][j-1]-1][i-1] == 0 and L[L[k-1][U[i-1][j-1]-1]-1][L[j-1][i-1]-1] != 0:
                            L[L[k-1][j-1]-1][i-1] = L[L[k-1][U[i-1][j-1]-1]-1][L[j-1][i-1]-1]
                            keepgoing = True
                        if L[L[k-1][j-1]-1][i-1] != L[L[k-1][U[i-1][j-1]-1]-1][L[j-1][i-1]-1]:
                            if L[L[k-1][j-1]-1][i-1] < L[L[k-1][U[i-1][j-1]-1]-1][L[j-1][i-1]-1] and not(tuple([L[L[k-1][j-1]-1][i-1],L[L[k-1][U[i-1][j-1]-1]-1][L[j-1][i-1]-1]]) in rlist):
                                rlist.append(tuple([L[L[k-1][j-1]-1][i-1],L[L[k-1][U[i-1][j-1]-1]-1][L[j-1][i-1]-1]]))
                            if L[L[k-1][j-1]-1][i-1] > L[L[k-1][U[i-1][j-1]-1]-1][L[j-1][i-1]-1] and not(tuple([L[L[k-1][U[i-1][j-1]-1]-1][L[j-1][i-1]-1],L[L[k-1][j-1]-1][i-1]]) in rlist):
                                rlist.append(tuple([L[L[k-1][U[i-1][j-1]-1]-1][L[j-1][i-1]-1],L[L[k-1][j-1]-1][i-1]]))
    return [U,L,rlist]




def bkeiratezero(M):
    ### returns best zero
    rm=[zeromatrix(len(M[0])),zeromatrix(len(M[0]))]
    U,L=M[0],M[1]
    out=False
    for i in range(1,len(U)+1):
        for j in range(1,len(U)+1):
            for k in range(1,len(U)+1):
                if U[j-1][k-1]==0: out=[0,j,k]
                if L[j-1][k-1]==0: out=[1,j,k]
                if U[k-1][j-1]==0 and L[i-1][j-1]!=0 and U[k-1][i-1]!=0 and U[j-1][i-1]!=0:
                    rm[0][k-1][j-1]=rm[0][k-1][j-1]+1
                if U[k-1][j-1]!=0 and L[i-1][j-1]==0 and U[k-1][i-1]!=0 and U[j-1][i-1]!=0:
                    rm[1][i-1][j-1]=rm[1][i-1][j-1]+1
                if U[k-1][j-1]!=0 and L[i-1][j-1]!=0 and U[k-1][i-1]==0 and U[j-1][i-1]!=0:
                    rm[0][k-1][i-1]=rm[0][k-1][i-1]+1
                if U[k-1][j-1]!=0 and L[i-1][j-1]!=0 and U[k-1][i-1]!=0 and U[j-1][i-1]==0:
                    rm[0][j-1][i-1]=rm[0][j-1][i-1]+1
                if U[j-1][i-1]==0 and U[k-1][i-1]!=0 and L[j-1][k-1]!=0 and L[i-1][k-1]!=0:
                    rm[0][j-1][i-1]=rm[0][j-1][i-1]+1
                if U[j-1][i-1]!=0 and U[k-1][i-1]==0 and L[j-1][k-1]!=0 and L[i-1][k-1]!=0:
                    rm[0][k-1][i-1]=rm[0][k-1][i-1]+1
                if U[j-1][i-1]!=0 and U[k-1][i-1]!=0 and L[j-1][k-1]==0 and L[i-1][k-1]!=0:
                    rm[1][j-1][k-1]=rm[1][j-1][k-1]+1
                if U[j-1][i-1]!=0 and U[k-1][i-1]!=0 and L[j-1][k-1]!=0 and L[i-1][k-1]==0:
                    rm[1][i-1][k-1]=rm[1][i-1][k-1]+1
                if L[i-1][j-1]==0 and U[k-1][j-1]!=0 and L[i-1][k-1]!=0 and L[j-1][k-1]!=0:
                    rm[1][i-1][j-1]=rm[1][i-1][j-1]+1
                if L[i-1][j-1]!=0 and U[k-1][j-1]==0 and L[i-1][k-1]!=0 and L[j-1][k-1]!=0:
                    rm[0][k-1][j-1]=rm[0][k-1][j-1]+1
                if L[i-1][j-1]!=0 and U[k-1][j-1]!=0 and L[i-1][k-1]==0 and L[j-1][k-1]!=0:
                    rm[1][i-1][k-1]=rm[1][i-1][k-1]+1
                if L[i-1][j-1]!=0 and U[k-1][j-1]!=0 and L[i-1][k-1]!=0 and L[j-1][k-1]==0:
                    rm[1][j-1][k-1]=rm[1][j-1][k-1]+1
                if U[i-1][j-1] != 0 and L[k-1][j-1] != 0 and U[i-1][L[k-1][j-1]-1] ==0 and U[j-1][k-1] != 0:
                    rm[0][i-1][L[k-1][j-1]-1]=rm[0][i-1][L[k-1][j-1]-1]+1
                if U[i-1][j-1] != 0 and L[k-1][j-1] != 0 and U[i-1][L[k-1][j-1]-1] !=0 and U[j-1][k-1] == 0:
                    rm[0][j-1][k-1]=rm[0][j-1][k-1]+1
                if L[k-1][j-1] == 0 and L[j-1][i-1]!= 0 and U[i-1][j-1] != 0 and L[k-1][U[i-1][j-1]-1] != 0:
                    rm[1][k-1][j-1]=rm[1][k-1][j-1]+1
                if L[k-1][j-1] != 0 and L[j-1][i-1]== 0 and U[i-1][j-1] != 0 and L[k-1][U[i-1][j-1]-1] != 0:
                    rm[1][j-1][i-1]=rm[1][j-1][i-1]+1
                if L[k-1][j-1] != 0 and L[j-1][i-1]!= 0 and U[i-1][j-1] != 0 and L[k-1][U[i-1][j-1]-1] == 0:
                    rm[1][k-1][U[i-1][j-1]-1]=rm[1][k-1][U[i-1][j-1]-1]+1
                if L[j-1][i-1] == 0 and U[i-1][j-1] != 0 and L[k-1][U[i-1][j-1]-1] !=0 and U[j-1][k-1] != 0 and L[k-1][j-1] != 0 and U[i-1][L[k-1][j-1]-1] != 0:
                    rm[1][j-1][i-1]=rm[1][j-1][i-1]+1
                if L[j-1][i-1] != 0 and U[i-1][j-1] != 0 and L[k-1][U[i-1][j-1]-1] ==0 and U[j-1][k-1] != 0 and L[k-1][j-1] != 0 and U[i-1][L[k-1][j-1]-1] != 0:
                    rm[1][k-1][U[i-1][j-1]-1]=rm[1][k-1][U[i-1][j-1]-1]+1
                if L[j-1][i-1] != 0 and U[i-1][j-1] != 0 and L[k-1][U[i-1][j-1]-1] !=0 and U[j-1][k-1] == 0 and L[k-1][j-1] != 0 and U[i-1][L[k-1][j-1]-1] != 0:
                    rm[0][j-1][k-1]=rm[0][j-1][k-1]+1
                if L[j-1][i-1] != 0 and U[i-1][j-1] != 0 and L[k-1][U[i-1][j-1]-1] !=0 and U[j-1][k-1] != 0 and L[k-1][j-1] != 0 and U[i-1][L[k-1][j-1]-1] == 0:
                    rm[1][i-1][L[k-1][j-1]-1]=rm[1][i-1][L[k-1][j-1]-1]+1
####
#            if M[0][i-1][j-1]==0:
#                return [0,i,j]
#                for z in range(1,len(M[0])+1):
#                    if M[0][x-1][z-1]!=0 and M[0][y-1][z-1]!=0:
#                        rm[0][x-1][y-1]=rm[0][x-1][y-1]+1
#                    if M[0][z-1][x-1]!=0 and M[0][z-1][y-1]!=0:
#                        rm[0][x-1][y-1]=rm[0][x-1][y-1]+1
#            if M[1][i-1][j-1]==0:
#                return[1,i,j]
#                for z in range(1,len(M)+1):
##                    if M[1][x-1][z-1]!=0 and M[1][y-1][z-1]!=0:
#                        rm[1][x-1][y-1]=rm[1][x-1][y-1]+1
#                    if M[1][z-1][x-1]!=0 and M[1][z-1][y-1]!=0:
#                        rm[1][x-1][y-1]=rm[1][x-1][y-1]+1
    st=0
    for x in range(1,len(M[0])+1):
        for y in range(1,len(M[0])+1):
            for i in range(0,2):
                if rm[i][x-1][y-1]>st:
                    out=[i,x,y]
                    st=rm[i][x-1][y-1]
    return out


def fgmbkei(M,L):
    ### complete finitely generated medial bikei table with up to L elements
    wm = [lm(M[0]),lm(M[1])]
    c=True
    while c:
        c=False
        while True:
            w=bgenreduce(mybfill2(wm))
            if w==wm:
                break
            wm=w
        f=bkeiratezero(wm)
        if not f:
            return wm
        else:
            wm=[lm(rcadd(wm[0])),lm(rcadd(wm[1]))]
            wm[f[0]][f[1]-1][f[2]-1]=len(wm[0])
            c=True
        if len(wm[0])>L:
            return wm
    return wm


def fgbkei(M,L):
    ### complete finitely generated bikei table with up to L elements
    wm = [lm(M[0]),lm(M[1])]
    c=True
    while c:
        c=False
        while True:
            w=bgenreduce(ybfill2(wm))
            if w==wm:
                break
            wm=w
        f=bkeiratezero(wm)
        if not f:
            return wm
        else:
            wm=[lm(rcadd(wm[0])),lm(rcadd(wm[1]))]
            wm[f[0]][f[1]-1][f[2]-1]=len(wm[0])
            c=True
        if len(wm[0])>L:
            return wm
    return wm


def g2bkpres(g):
    ### convert gauss code to biquandle presentation matrix
    L=0
    for x in g:
       L=L+len(x)       
    out=[zeromatrix(L),zeromatrix(L)]
    PD=gauss2pd(g)
    rlist=[]
    for x in PD:
        if x[0]==1:
            if out[0][x[1]-1][x[4]-1]==0:
                out[0][x[1]-1][x[4]-1]=x[3]
            if out[0][x[1]-1][x[4]-1]<x[3] and not(tuple([out[0][x[1]-1][x[4]-1],x[3]]) in rlist):
                rlist.append(tuple([out[0][x[1]-1][x[4]-1],x[3]]))
            if out[0][x[1]-1][x[4]-1]>x[3] and not(tuple([x[3],out[0][x[1]-1][x[4]-1]]) in rlist):
                rlist.append(tuple([x[3],out[0][x[1]-1][x[4]-1]]))
            if out[1][x[4]-1][x[1]-1]==0:
                out[1][x[4]-1][x[1]-1]=x[2]
            if out[1][x[4]-1][x[1]-1]<x[2] and not(tuple([out[1][x[4]-1][x[1]-1],x[2]]) in rlist):
                rlist.append(tuple([out[1][x[4]-1][x[1]-1],x[2]]))
            if out[1][x[4]-1][x[1]-1]>x[2] and not(tuple([x[2],out[1][x[4]-1][x[1]-1]]) in rlist):
                rlist.append(tuple([x[2],out[1][x[4]-1][x[1]-1]]))
            if out[0][x[3]-1][x[2]-1]==0:
                out[0][x[3]-1][x[2]-1]=x[1]
            if out[0][x[3]-1][x[2]-1]<x[1] and not(tuple([out[0][x[3]-1][x[2]-1],x[1]]) in rlist):
                rlist.append(tuple([out[0][x[3]-1][x[2]-1],x[1]]))
            if out[0][x[3]-1][x[2]-1]>x[1] and not(tuple([x[1],out[0][x[3]-1][x[2]-1]]) in rlist):
                rlist.append(tuple([x[1],out[0][x[3]-1][x[2]-1]]))
            if out[1][x[2]-1][x[3]-1]==0:
                out[1][x[2]-1][x[3]-1]=x[4]
            if out[1][x[2]-1][x[3]-1]<x[4] and not(tuple([out[1][x[2]-1][x[3]-1],x[4]]) in rlist):
                rlist.append(tuple([out[1][x[2]-1][x[3]-1],x[4]]))
            if out[1][x[2]-1][x[3]-1]>x[4] and not(tuple([x[4],out[1][x[2]-1][x[3]-1]]) in rlist):
                rlist.append(tuple([x[4],out[0][x[2]-1][x[3]-1]]))
        if x[0]==-1:
            if out[0][x[3]-1][x[2]-1]==0:
                out[0][x[3]-1][x[2]-1]=x[1]
            if out[0][x[3]-1][x[2]-1]<x[1] and not(tuple([out[0][x[3]-1][x[2]-1],x[1]]) in rlist):
                rlist.append(tuple([out[0][x[3]-1][x[2]-1],x[1]]))
            if out[0][x[3]-1][x[2]-1]>x[1] and not(tuple([x[1],out[0][x[3]-1][x[2]-1]]) in rlist):
                rlist.append(tuple([x[1],out[0][x[3]-1][x[2]-1]]))
            if out[1][x[2]-1][x[3]-1]==0:
                out[1][x[2]-1][x[3]-1]=x[4]
            if out[1][x[2]-1][x[3]-1]<x[4] and not(tuple([out[1][x[2]-1][x[3]-1],x[4]]) in rlist):
                rlist.append(tuple([out[1][x[2]-1][x[3]-1],x[4]]))
            if out[1][x[2]-1][x[3]-1]>x[4] and not(tuple([x[4],out[1][x[2]-1][x[3]-1]]) in rlist):
                rlist.append(tuple([x[4],out[1][x[2]-1][x[3]-1]]))
            if out[0][x[1]-1][x[4]-1]==0:
                out[0][x[1]-1][x[4]-1]=x[3]
            if out[0][x[1]-1][x[4]-1]<x[3] and not(tuple([out[0][x[1]-1][x[4]-1],x[3]]) in rlist):
                rlist.append(tuple([out[0][x[1]-1][x[4]-1],x[3]]))
            if out[0][x[1]-1][x[4]-1]>x[3] and not(tuple([x[3],out[0][x[1]-1][x[4]-1]]) in rlist):
                rlist.append(tuple([x[3],out[0][x[1]-1][x[4]-1]]))
            if out[1][x[4]-1][x[1]-1]==0:
                out[1][x[4]-1][x[1]-1]=x[2]
            if out[1][x[4]-1][x[1]-1]<x[2] and not(tuple([out[1][x[4]-1][x[1]-1],x[2]]) in rlist):
                rlist.append(tuple([out[1][x[4]-1][x[1]-1],x[2]]))
            if out[1][x[4]-1][x[1]-1]>x[2] and not(tuple([x[2],out[1][x[4]-1][x[1]-1]]) in rlist):
                rlist.append(tuple([x[2],out[1][x[4]-1][x[1]-1]]))
    return bgenreduce(tuple([out[0],out[1],rlist]))



##############################
# Gauss code table
##############################

gknot = {
  (0):[[-1,1]],
(3,1):[[-1,2,-3,1,-2,3]],
(4,1):[[-1.5,2.5,-3,4,-2.5,1.5,-4,3]],
(5,1):[[-1,2,-3,4,-5,1,-2,3,-4,5]],
(5,2):[[-1,2,-3,4,-5,3,-2,1,-4,5]],
(6,1):[[-1,2,-3.5,4.5,-5.5,6.5,-2,1,-6.5,5.5,-4.5,3.5]],
(6,2):[[-1,2.5,-3.5,4.5,-5.5,1,-6,3.5,-4.5,5.5,-2.5,6]],
(6,3):[[1,-2.5,3.5,-4.5,2.5,-5,6,-1,5,-3.5,4.5,-6]],
#(6,3):[[-1,2,-3.5,4.5,-5.5,1,-6.5,3.5,-4.5,6.5,-2,5.5]],
(6,4):[[-1,2,-3,1,-2,3,-4,5,-6,4,-5,6]],
(6,5):[[-1,2,-3,1,-2,3,4.5,-5.5,6.5,-4.5,5.5,-6.5]],
(7,1):[[-1,2,-3,4,-5,6,-7,1,-2,3,-4,5,-6,7]],
(7,2):[[-1.5,6.5,-7.5,1.5,-2.5,3.5,-4.5,5.5,-6.5,7.5,-5.5,4.5,-3.5,2.5]],
(7,3):[[-1,2,-3,4,-7,6,-5,1,-2,3,-4,5,-6,7]],
(7,4):[[-1,2,-3,4,-5,6,-7,1,-4,3,-2,7,-6,5]],
(7,5):[[-1.5,2.5,-3.5,4.5,-5.5,1.5,-2.5,3.5,-6.5,7.5,-4.5,5.5,-7.5,6.5]],
(7,6):[[-1.5,2.5,-3,4,-5.5,6.5,-4,3,-7.5,1.5,-6.5,5.5,-2.5,7.5]],
(7,7):[[-1.5,2.5,-3,4,-2.5,5.5,-6,7,-5.5,1.5,-4,3,-7,6]],
(8,1):[[-1.5,2.5,-3,4,-2.5,1.5,-5.5,6.5,-7.5,8.5,-4,3,-8.5,7.5,-6.5,5.5]],
(8,2):[[1,-2,3.5,-4.5,5.5,-6.5,7.5,-8.5,2,-1,8.5,-3.5,4.5,-5.5,6.5,-7.5]],
(8,3):[[-1,2,-3,4,-5.5,6.5,-7.5,8.5,-4,3,-2,1,-8.5,7.5,-6.5,5.5]],
(8,4):[[-1.5,2,-3,4,-5,1.5,-6.5,7.5,-8.5,5,-4,3,-2,6.5,-7.5,8.5]],
(8,5):[[-1.5,2.5,-3,4,-5,6,-7,8,-2.5,1.5,-6,7,-8,3,-4,5]],
(8,6):[[1,-2,3.5,-4.5,5.5,-6.5,7.5,-8.5,2,-1,8.5,-7.5,6.5,-3.5,4.5,-5.5]],
(8,7):[[-1.5,2.5,-3.5,1.5,-4,5,-6,7,-8,4,-2.5,3.5,-5,6,-7,8]],
(8,8):[[1,-2,3,-4.5,5.5,-6.5,4.5,-7,8,-5.5,6.5,-3,2,-1,7,-8]],
(8,9):[[-1.5,2.5,-3.5,4.5,-5,6,-7,8,-2.5,3.5,-4.5,1.5,-8,5,-6,7]],
#(8,10):[[-1,2,-3,4,-5,6,-7,1,-2,8.5,-6,7,-8.5,3,-4,5]],
(8,10):[[-1,2,-3,4,-5,1,-2,6.5,-7.5,3,-4,8.5,-6.5,7.5,-8.5,5]],
(8,11):[[1,-2,3.5,-4.5,5.5,-6.5,7.5,-8.5,2,-1,8.5,-5.5,4.5,-3.5,6.5,-7.5]],
(8,12):[[-1,2,-3,4,-5.5,6.5,-4,3,-7.5,8.5,-2,1,-8.5,7.5,-6.5,5.5]],
(8,13):[[1.5,-2.5,3,-4,5,-6,7,-3,8.5,-1.5,2.5,-8.5,4,-7,6,-5]],
(8,14):[[-1,2,-3.5,4.5,-5.5,6.5,-7.5,5.5,-4.5,8.5,-2,1,-6.5,7.5,-8.5,3.5]],
(8,15):[[1.5,-2.5,3.5,-4.5,5.5,-3.5,6.5,-7.5,8.5,-6.5,2.5,-1.5,7.5,-8.5,4.5,-5.5]],
(8,16):[[1.5,-2,3,-4.5,5.5,-6,2,-7.5,4.5,-5.5,8.5,-1.5,7.5,-3,6,-8.5]],
#(8,17):[[1.5,-2.5,3,-4,5.5,-1.5,6.5,-3,4,-7.5,8.5,-5.5,2.5,-6.5,7.5,-8.5]],
(8,17):[[-1.5,2.5,-3,4,-5,6,-2.5,7.5,-4,5,-8.5,1.5,-6,3,-7.5,8.5]],
(8,18):[[-1,2.5,-3.5,4,-5,6.5,-2.5,7,-4,8.5,-6.5,1,-7,3.5,-8.5,5]],
(8,19):[[-1,2,-3,-4,5,1,-2,-6,4,7,-8,-5,6,3,-7,8]],
(8,20):[[-1,2.5,3,-4,-5.5,1,6.5,-3,4,-7.5,8.5,5.5,-2.5,-6.5,7.5,-8.5]],
(8,21):[[-1,2.5,-3.5,-4.5,5.5,-6,-7.5,1,4.5,-5.5,8.5,7.5,-2.5,3.5,6,-8.5]],
(9,2):[[-1.5,2.5,-3.5,4.5,-5.5,6.5,-7.5,8.5,-9.5,1.5,-2.5,9.5,-8.5,7.5,-6.5,5.5,-4.5,3.5]],
(9,24):[[-1.5,2.5,-3,4.5,-5.5,6,-7,8,-2.5,1.5,-6,7,-8,9.5,-4.5,5.5,-9.5,3]],
(9,32):[[-1.5,2.5,-3,4,-5,6,-7,8,-2.5,9.5,-4,7,-8,3,-9.5,1.5,-6,5]],
(10,132):[[1.5,-2.5,3.5,-1.5,-4,5.5,6,-7.5,-8,4,9.5,-6,-10.5,8,2.5,-3.5,7.5,10.5,-5.5,-9.5]],
#(11,34):[[-1,2,-3,4.5,-5.5,6.5,-7.5,1,-8.5,9.5,-2,3,-10.5,8.5,-9.5,10.5,-11,7.5,-4.5,5.5,-6.5,11]],
(11,1):[[-1,2.5,-3.5,-4,5,6.5,-2.5,7,-8,3.5,-6.5,1,-7,8,9.5,-10.5,11.5,-5,4,-9.5,10.5,-11.5]],
(11,2):[[-1,2.5,-3.5,-4.5,5.5,-6.5,7,-8,4.5,-5.5,6.5,9.5,-2.5,10,-11,3.5,-9.5,1,-10,11,8,-7]],
#(11,34):[[-1,2,-3,4.5,5.5,-6.5,7.5,-5.5,8,-9,6.5,-7.5,-10.5,3,-11,-8,9,1,-2,10.5,-4.5,11]],
(11,42):[[-1,2,3.5,-4,5,-6,7,-3.5,8.5,-5,6,9.5,-10.5,11.5,-9.5,1,-2,10.5,-11.5,-7,4,-8.5]]
}

gknotlist=((0),(3,1),(4,1),(5,1),(5,2),(6,1),(6,2),(6,3),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(7,7),(8,1),(8,2),(8,3),(8,4),(8,5),(8,6),(8,7),(8,8),(8,9),(8,10),(8,11),(8,12),(8,13),(8,14),(8,15),(8,16),(8,17),(8,18),(8,19),(8,20),(8,21))

glinklist=((2,0,1),(4,0,1),(5,0,1),(6,0,1),(6,0,2),(6,0,3),(6,0,4),(6,0,5),(6,1,1),(7,0,1),(7,0,2),(7,0,3),(7,0,4),(7,0,5),(7,0,6),(7,0,7),(7,1,1),(7,1,2))

glink = {
(0,2):[[-1,1],[-2,2]],
(0,3):[[-1,1],[-2,2],[-3,3]],
(2,0,1):[[-1,2],[-2,1]],
(4,0,1):[[-1,2,-3,4],[-4,3,-2,1]],
(5,0,1):[[-1,2.5,-3.5,4],[1,-4,5.5,-2.5,3.5,-5.5]],
(6,0,1):[[-1,2,-3,4],[1,-5.5,6.5,-4,3,-6.5,5.5,-2]],
#(6,0,2):[[-1,2,-5.5,4,-3.5,6],[1,-2,3.5,-4,5.5,-6]],
(6,0,2):[[-1,2,-3,4,-5,6],[1,-2,3,-6,5,-4]],
(6,0,3):[[-1,2,-3,4,-5,6],[1,-2,3,-4,5,-6]],
(6,0,4):[[-1,2,-3,4],[-5,1,-6,3],[-2,6,-4,5]],
#(6,0,5):[[-1,2.5,-3.5,4],[1,-5,6,-2.5],[3.5,-6,5,-4]],
(6,0,5):[[-1,2,-3,4],[1,-5,6,-2],[3,-6,5,-4]],
(6,1,1):[[-1,-2,3,4],[1,-5,-3,6],[2,5,-4,-6]],
(7,0,1):[[-1.5,2.5,-3,4,-5.5,1.5,-6,3,-7.5,5.5],[-2.5,7.5,-4,6]],
(7,0,2):[[-1,2,-3,4,-5,1,-2,5,-6,7],[3,-7,6,-4]],
(7,0,3):[[-1.5,2.5,-3.5,4.5,-5.5,1.5,-2.5,3.5,-6,7],[-4.5,5.5,-7,6]],
(7,0,4):[[-1.5,2.5,-3.5,4.5,-5.5,3.5,-2.5,1.5,-6,7],[-4.5,5.5,-7,6]],
(7,0,5):[[-1,2.5,-3.5,1,-4,5,-6,7],[-2.5,4,-7,6,-5,3.5]],
(7,0,6):[[-1,2.5,-3.5,4.5,-2.5,5,-6,7],[1,-7,6,-5,3.5,-4.5]],
(7,0,7):[[-1,2,-3,4],[1,-5.5,6.5,-2],[3,-7.5,5.5,-6.5,7.5,-4]],
(7,1,1):[[-1,2.5,3,-4.5,-5,1,6.5,-3,-7.5,5],[-2.5,-6.5,4.5,7.5]],
(7,1,2):[[-1,2.5,3,-4.5,-5,1,-6,-3,7,5],[-2.5,6,4.5,-7]]
#2.4:[[-1,4,-5,6,-3,2],[1,-2,3,-4,5,-6]],
#2.5:[[-1,2,-3,4,-5,6,-7,8],[1,-2,3,-8,7,-4,5,-6]],
#3.1:[[-1,2],[-2,1],[-3,3]],
#3.2:[[-1,2],[-2,3,-4,1],[-3,4]],
}


gvknot = {
(2,1):[[-1,2,1,-2]],
(3,1):[[-1.5,2,-3.5,-2,1.5,3.5]],
(3,2):[[-1.5,2.5,-3,-2.5,1.5,3]],
(3,3):[[-1.5,-2.5,-3.5,2.5,1.5,3.5]],
(3,4):[[-1.5,-2.5,-3,2.5,1.5,3]],
(3,5):[[-1.5,-2.5,-3.5,1.5,2.5,3.5]],
(3,6):[[-1,2,-3,1,-2,3]],
(3,7):[[-1.5,2.5,-3,1.5,-2.5,3]],
(4,1):[[1.5,2.5,-1.5,-2.5,3.5,4.5,-3.5,-4.5]],
(4,2):[[1.5,2.5,-1.5,-2.5,3,4,-3,-4]],
(4,3):[[1.5,2.5,-1.5,-2.5,3.5,-4.5,-3.5,4.5]],
(4,4):[[1.5,2.5,-1.5,-2.5,3.5,-4,-3.5,4]],
(4,5):[[1.5,2.5,-1.5,-2.5,3,-4.5,-3,4.5]],
(4,6):[[1.5,2.5,-1.5,-2.5,3,-4,-3,4]],
(4,7):[[1.5,2.5,-1.5,-2.5,-3.5,-4.5,3.5,4.5]],
(4,8):[[1.5,2.5,-1.5,-2.5,-3,-4,3,4]],
(4,9):[[1.5,2.5,-1.5,3.5,-2.5,4.5,-3.5,-4.5]],
(4,10):[[1.5,2.5,-1.5,3.5,-2.5,4,-3.5,-4]],
(4,11):[[1.5,2.5,-1.5,3,-2.5,4.5,-3,-4.5]],
(4,12):[[1.5,2.5,-1.5,3,-2.5,4,-3,-4]],
(4,13):[[1.5,2,-1.5,3.5,-2,4,-3.5,-4]],
(4,14):[[1.5,2,-1.5,3,-2,4.5,-3,-4.5]],
(4,15):[[1.5,2.5,-1.5,3.5,-2.5,-4.5,-3.5,4.5]],
(4,16):[[1.5,2.5,-1.5,3.5,-2.5,-4,-3.5,4]],
(4,17):[[1.5,2.5,-1.5,3,-2.5,-4,-3,4]],
(4,18):[[1.5,2,-1.5,3.5,-2,-4.5,-3.5,4.5]],
(4,19):[[1.5,2,-1.5,3.5,-2,-4,-3.5,4]],
(4,20):[[1.5,2,-1.5,3,-2,-4.5,-3,4.5]],
(4,21):[[1.5,2,-1.5,3,-2,-4,-3,4]],
(4,22):[[1.5,2.5,-1.5,3,4,-2.5,-3,-4]],
(4,23):[[1.5,2,-1.5,3.5,4.5,-2,-3.5,-4.5]],
(4,24):[[1.5,2,-1.5,3,4,-2,-3,-4]],
(4,25):[[1.5,2.5,-1.5,3.5,4.5,-2.5,-4.5,-3.5]],
(4,26):[[1.5,2.5,-1.5,3,4,-2.5,-4,-3]],
(4,27):[[1.5,2,-1.5,3.5,4.5,-2,-4.5,-3.5]],
(4,28):[[1.5,2,-1.5,3,4,-2,-4,-3]],
(4,29):[[1.5,2.5,-1.5,3.5,4.5,-3.5,-2.5,-4.5]],
(4,30):[[1.5,2.5,-1.5,3.5,4,-3.5,-2.5,-4]],
(4,31):[[1.5,2.5,-1.5,3,4.5,-3,-2.5,-4.5]],
(4,32):[[1.5,2.5,-1.5,3,4,-3,-2.5,-4]],
(4,33):[[1.5,2,-1.5,3.5,4.5,-3.5,-2,-4.5]],
(4,34):[[1.5,2,-1.5,3.5,4,-3.5,-2,-4]],
(4,35):[[1.5,2,-1.5,3,4.5,-3,-2,-4.5]],
(4,36):[[1.5,2,-1.5,3,4,-3,-2,-4]],
(4,37):[[1.5,2.5,-1.5,3.5,-4.5,-2.5,-3.5,4.5]],
(4,38):[[1.5,2.5,-1.5,3.5,-4,-2.5,-3.5,4]],
(4,39):[[1.5,2.5,-1.5,3,-4.5,-2.5,-3,4.5]],
(4,40):[[1.5,2.5,-1.5,3,-4,-2.5,-3,4]],
(4,41):[[1.5,2,-1.5,3.5,-4.5,-2,-3.5,4.5]],
(4,42):[[1.5,2,-1.5,3,-4.5,-2,-3,4.5]],
(4,43):[[1.5,2.5,-1.5,3.5,-4.5,-2.5,4.5,-3.5]],
(4,44):[[1.5,2.5,-1.5,3.5,-4,-2.5,4,-3.5]],
(4,45):[[1.5,2.5,-1.5,3,-4.5,-2.5,4.5,-3]],
(4,46):[[1.5,2.5,-1.5,3,-4,-2.5,4,-3]],
(4,47):[[1.5,2,-1.5,3,-4.5,-2,4.5,-3]],
(4,48):[[1.5,2.5,-1.5,3.5,-4.5,-3.5,-2.5,4.5]],
(4,49):[[1.5,2.5,-1.5,3.5,-4,-3.5,-2.5,4]],
(4,50):[[1.5,2.5,-1.5,3,-4.5,-3,-2.5,4.5]],
(4,51):[[1.5,2.5,-1.5,3,-4,-3,-2.5,4]],
(4,52):[[1.5,2,-1.5,3.5,-4,-3.5,-2,4]],
(4,53):[[1.5,2.5,-1.5,3.5,-4.5,-3.5,4.5,-2.5]],
(4,54):[[1.5,2.5,-1.5,3.5,-4,-3.5,4,-2.5]],
(4,55):[[1.5,2,-1.5,3.5,-4,-3.5,4,-2]],
(4,56):[[1.5,2,-1.5,3,-4.5,-3,4.5,-2]],
(4,57):[[1.5,2.5,-1.5,-3.5,-2.5,-4,3.5,4]],
(4,58):[[1.5,2.5,-1.5,-3,-2.5,-4,3,4]],
(4,59):[[1.5,2,-1.5,-3.5,-2,-4,3.5,4]],
(4,60):[[1.5,2,-1.5,-3,-2,-4.5,3,4.5]],
(4,61):[[1.5,2.5,-1.5,-3.5,4.5,-2.5,3.5,-4.5]],
(4,62):[[1.5,2.5,-1.5,-3.5,4,-2.5,3.5,-4]],
(4,63):[[1.5,2.5,-1.5,-3,4.5,-2.5,3,-4.5]],
(4,64):[[1.5,2.5,-1.5,-3,4,-2.5,3,-4]],
(4,65):[[1.5,2,-1.5,-3.5,4.5,-2,3.5,-4.5]],
(4,66):[[1.5,2,-1.5,-3.5,4,-2,3.5,-4]],
(4,67):[[1.5,2,-1.5,-3,4.5,-2,3,-4.5]],
(4,68):[[1.5,2,-1.5,-3,4,-2,3,-4]],
(4,69):[[1.5,2.5,-1.5,-3.5,4.5,3.5,-2.5,-4.5]],
(4,70):[[1.5,2.5,-1.5,-3,4.5,3,-2.5,-4.5]],
(4,71):[[1.5,2.5,-1.5,-3,4,3,-2.5,-4]],
(4,72):[[1.5,2,-1.5,-3,4.5,3,-2,-4.5]],
(4,73):[[1.5,2.5,-1.5,-3.5,4.5,3.5,-4.5,-2.5]],
(4,74):[[1.5,2.5,-1.5,-3.5,4,3.5,-4,-2.5]],
(4,75):[[1.5,2.5,-1.5,-3,4,3,-4,-2.5]],
(4,76):[[1.5,2,-1.5,-3.5,4,3.5,-4,-2]],
(4,77):[[1.5,2,-1.5,-3,4.5,3,-4.5,-2]],
(4,78):[[1.5,2.5,-1.5,-3.5,-4.5,-2.5,3.5,4.5]],
(4,79):[[1.5,2,-1.5,-3.5,-4.5,-2,3.5,4.5]],
(4,80):[[1.5,2.5,-1.5,-3.5,-4.5,-2.5,4.5,3.5]],
(4,81):[[1.5,2,-1.5,-3.5,-4.5,-2,4.5,3.5]],
(4,82):[[1.5,2.5,3.5,-1.5,4.5,-2.5,-3.5,-4.5]],
(4,83):[[1.5,2.5,3.5,-1.5,4,-2.5,-3.5,-4]],
(4,84):[[1.5,2,3,-1.5,4.5,-2,-3,-4.5]],
(4,85):[[1.5,2.5,3.5,-1.5,4,-3.5,-2.5,-4]],
(4,86):[[1.5,2,3,-1.5,4.5,-3,-2,-4.5]],
(4,87):[[1.5,2.5,3.5,-1.5,-4.5,-2.5,-3.5,4.5]],
(4,88):[[1.5,2,3,-1.5,-4.5,-2,-3,4.5]],
(4,89):[[1.5,2.5,3.5,-1.5,-4.5,-3.5,-2.5,4.5]],
(4,90):[[1.5,2,3,-1.5,-4.5,-3,-2,4.5]],
(4,91):[[1.5,2.5,3.5,4.5,-1.5,-2.5,-3.5,-4.5]],
(4,92):[[1.5,2.5,3.5,4.5,-1.5,-3.5,-2.5,-4.5]],
(4,93):[[1.5,2.5,3.5,4,-1.5,-3.5,-2.5,-4]],
(4,94):[[1.5,2.5,-3.5,-1.5,4.5,-2.5,3.5,-4.5]],
(4,95):[[1.5,2.5,-3.5,-1.5,4,-2.5,3.5,-4]],
(4,96):[[1.5,2.5,-3,-1.5,4.5,-2.5,3,-4.5]],
(4,97):[[1.5,2.5,-3,-1.5,4,-2.5,3,-4]],
(4,98):[[1.5,2.5,-3,-1.5,4,3,-2.5,-4]],
(4,99):[[1.5,2,-3,-1.5,4.5,3,-2,-4.5]],
(4,100):[[1.5,2.5,-3.5,4.5,-1.5,-2.5,3.5,-4.5]],
(4,101):[[1.5,2.5,-3.5,4,-1.5,-2.5,3.5,-4]],
(4,102):[[1.5,2.5,-3,4,-1.5,-2.5,3,-4]],
(4,103):[[1.5,2.5,-3.5,4,-2.5,-1.5,3.5,-4]],
(4,104):[[1.5,2.5,-3,4,-2.5,-1.5,3,-4]],
(4,105):[[1.5,-2.5,3.5,-1.5,4.5,-3.5,2.5,-4.5]],
(4,106):[[1.5,-2.5,3.5,-1.5,4,-3.5,2.5,-4]],
(4,107):[[1.5,-2.5,3,-1.5,4,-3,2.5,-4]],
(4,108):[[1.5,-2,3,-1.5,4.5,-3,2,-4.5]],
#slavik
(5,1):[[-1,2,-3.5,4.5,-2,1,-5.5,3.5,-4.5,5.5]],
#miyazawa
(5,2):[[-1,-2.5,3,-4,2.5,4,1,-3]]}



gvknotlist = ((2,1),(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),(3,7),(4,1),(4,2),(4,3),(4,4),(4,5),(4,6),(4,7),(4,8),(4,9),(4,10),(4,11),(4,12),(4,13),(4,14),(4,15),(4,16),(4,17),(4,18),(4,19),(4,20),(4,21),(4,22),(4,23),(4,24),(4,25),(4,26),(4,27),(4,28),(4,29),(4,30),(4,31),(4,32),(4,33),(4,34),(4,35),(4,36),(4,37),(4,38),(4,39),(4,40),(4,41),(4,42),(4,43),(4,44),(4,45),(4,46),(4,47),(4,48),(4,49),(4,50),(4,51),(4,52),(4,53),(4,54),(4,55),(4,56),(4,57),(4,58),(4,59),(4,60),(4,61),(4,62),(4,63),(4,64),(4,65),(4,66),(4,67),(4,68),(4,69),(4,70),(4,71),(4,72),(4,73),(4,74),(4,75),(4,76),(4,77),(4,78),(4,79),(4,80),(4,81),(4,82),(4,83),(4,84),(4,85),(4,86),(4,87),(4,88),(4,89),(4,90),(4,91),(4,92),(4,93),(4,94),(4,95),(4,96),(4,97),(4,98),(4,99),(4,100),(4,101),(4,102),(4,103),(4,104),(4,105),(4,106),(4,107),(4,108))


def gauss2pd(G):
    ###convert Gauss code to planar diagram###
    out = []
    semiarccount = 0
    complen = []
    for i in range(0,len(G)):
        semiarccount = semiarccount + len(G[i])
        complen.append(len(G[i]))
    nx, cr = [], [] 
    for k in range(0,semiarccount):
        nx.append(0)
        cr.append(0)
    current = 1
    i = 0
    for x in range(1,len(G)+1):
        for y in range(1,len(G[x-1])+1):
            i = i+1
            if y == complen[x-1]:
                nx[i-1] = current
            else:
                nx[i-1] = i+1
            j = 0
            for z in range(1,len(G)+1):
                for w in range(1,len(G[z-1])+1):
                    j = j +1
                    if G[z-1][w-1] + G[x-1][y-1] == 0:
                        cr[i-1] = j 
        current = current + complen[x-1]
    i = 0
    for x in range(1,len(G)+1):
        for y in range(1,len(G[x-1])+1):
            i = i+1
            if G[x-1][y-1] < 0:
                if G[x-1][y-1] % 1 == 0:
                    out.append([ 1,i,nx[cr[i-1]-1],nx[i-1],cr[i-1] ])
                else:
                    out.append([-1,i,cr[i-1],nx[i-1],nx[cr[i-1]-1] ])
    return out

def rcadd(M):
    # add a row and column to matrix
    out=[]
    for x in range(0,len(M)):
        temp=[]
        for y in range(0,len(M[0])):
            temp.append(M[x][y])
        temp.append(0)
        out.append(temp)
    temp=[]
    for x in range(0,len(out[0])):
        temp.append(0)
    out.append(temp)
    return out


def bisotest(M,N):
    ###test for biquandle isomorphism###
    z = []
    for i in range(1,len(M[0])+1): z.append(0)
    L,out = [z],[]
    while len(L) != 0:
        w = L[0]
        L[0:1] = []  
        i = hfindzero(w)
        if (not i) and permtest(w): return True
        else:
            for j in pavail(w):
                phi = list(w)
                phi[i-1] = j
                v = bisofill(M,N,phi)
                if v: L.append(tuple(v))
    return False

def bisofill(M,N,f):
    ### fill isomorphism f:M -> N ###
    m,n = len(M[0]), len(N[0])
    if m != n: return False
    keepgoing = True
    while keepgoing:
        keepgoing = False
        for i in range(1,n+1):
            for j in range(1,n+1):
                if f[i-1] !=0 and f[j-1] != 0:
                    if f[M[0][i-1][j-1]-1] == 0: 
                        f[M[0][i-1][j-1]-1] = N[0][f[i-1]-1][f[j-1]-1]
                        keepgoing = True
                    if N[0][f[i-1]-1][f[j-1]-1] != f[M[0][i-1][j-1]-1]: return False
                    if f[M[1][i-1][j-1]-1] == 0: 
                        f[M[1][i-1][j-1]-1] = N[1][f[i-1]-1][f[j-1]-1]
                        keepgoing = True
                    if N[1][f[i-1]-1][f[j-1]-1] != f[M[1][i-1][j-1]-1]: return False
    if reptest(f): return f
    return False

def pavail(v):
    ### List available entries ###
    L = []
    for i in range(1,len(v)+1):
        if not i in v: L.append(i)
    return tuple(L)

def hfindzero(f):   
    ### find zero in homomorphism template ###
    j = -1
    for i in range(0,len(f)):
        if f[i] == 0: 
            j = i+1
            break
    if j < 0: out = False
    else: out = j
    return out

def breducelist(L):
    ###Remove isomorphic copies from L###
    out = [tm(L[0])]
    W = L
    while len(W)>0:
        x = W[0]
        W[0:1] = []
        newbiq = True
        for y in out:
            if bisotest(x,y): newbiq = False
        if newbiq: out.append(tm(x))
    return out

def reptest(p):   
    ### Test whether p has repeated non-zero entries ###
    q = True
    L = []
    for i in range(1,len(p)+1):
        if p[i-1] != 0:
            if p[i-1] in L:
                q = False
            else:
                L.append(p[i-1])
    return q

def permtest(p):   # test whether p is a permutation
    ### Test whether p is a permutation### 
    q = True
    for i in range(1,len(p)+1):
        if not i in p:
            q = False
    return q


def abq(n,s,t):
    ###Alexander biquandle Z_n###
    U,L=zeromatrix(n),zeromatrix(n)
    for i in range(1,n+1):
       for j in range(1,n+1):
           U[i-1][j-1] = (t*i+(s-s)*j) %n 
           L[i-1][j-1] = (s*i %n) 
    for i in range(1,n+1):
       for j in range(1,n+1):
           if U[i-1][j-1] == 0: U[i-1][j-1] = n
           if L[i-1][j-1] == 0: L[i-1][j-1] = n
    return([U,L])
