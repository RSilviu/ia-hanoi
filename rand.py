from random import randrange
from general import *


def strategie(SC):
    npasi = 0
    # bune si rele?
    stari = {SC}
    stari_init = {SC}
    stari_bune = {SC}
    stari_inv = dict()
    stari_moarte = dict()
    while not st_finala(SC,SF):
        # in (1,i) if sc[j] in (i,m+1)=3
        i = 0
        # nu muta piesele asezate corect
        for j in range(1,m+1):
            if SC[j:] == [3]*(m-j+1):
                i = j
                break

        # posibil sa nu pot iesi => bt random n pasi inapoi
        repeta = True
        while repeta:
            piesa = randrange(1,i) if i else randrange(1, m + 1)
            tija = randrange(1,n+1)
            SA = tranzitie(SC,piesa,tija)
            # print(SA)
            npasi += 1
            if SA not in stari_moarte.get(tuple(SC),SC):
                stari[tuple(SC)].append(SA)
                repeta = False

        if validare(SC,SA,piesa):
            SC = SA
            print(SC)
            # stari.append(list(SC))
            # npasi += 1
        else:
            stari_inv |= {SA}
            # SC = stari[randrange(0,len(stari))]

    # print('#stari bune:',len(stari))
    return npasi

n,m = 3,3

SI = [None]+[1]*m
SF = [None]+[3]*m
print(n,'tije,',m,'obiecte,','random (#pasi):',strategie(SI))













