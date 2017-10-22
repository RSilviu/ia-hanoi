from random import randrange
from general import *


def strategie(SC):
    npasi = 0   # incercari totale
    tranzitii = 0   # tranzitii totale
    stari_acceptate = 0 #stari totale acceptate
    stari_valide = [SC]
    alegeri = dict()
    stare_noua = True
    print(SC[1:])
    while not st_finala(SC,SF):
        if stare_noua: i = piesa_urmatoare(SC,m,n)       # nu muta piesele asezate corect
        # sc -> sa iff mai sunt stari din sc
        piese_disp = i - 1 if i else m
        aleg_tot = 1 + (n - 1) * piese_disp
        tsc = tuple(SC)
        alegeri[tsc] = alegeri.get(tsc, [SC])
        if len(alegeri[tsc]) >= aleg_tot:
            # mergem inapoi random
            idx_inapoi = randrange(len(stari_valide))
            print('Inapoi la starea', idx_inapoi)
            SC = stari_valide[idx_inapoi]
            stare_noua = True
            continue
        piesa,tija=[None]*2
        SA = None
        repeta = True
        while repeta:
            piesa = randrange(1,i) if i else randrange(1, m + 1)
            tija = randrange(1,n+1)
            npasi += 1
            # alegere = (piesa,tija)
            # alegeri[tsc] = alegeri.get(tsc,set([(idx,SC[idx]) for idx in range(1,len(SC))]))
            # if alegere not in alegeri[tsc]:
            #     alegeri[tsc] |= {alegere}
            #     repeta = False
            SA = tranzitie(list(SC), piesa, tija)
            if SA not in alegeri[tsc]:
                tranzitii += 1
                alegeri[tsc].append(SA)
                repeta = False
        if validare(SC,SA,piesa) and (SA not in stari_valide):
            stari_acceptate += 1
            stari_valide.append(SA)
            SC = SA
            stare_noua = True
            print(SC[1:])
        else: stare_noua = False   # SA invalida
            # print('Invalida',SA[1:])
    # print('#stari bune:',len(stari))
    return (npasi,tranzitii,stari_acceptate)

n,m = 4,3

SI = [None]+[1]*m
SF = [None]+[n]*m
print((str(n)+' tije, '+str(m)+' obiecte').center(50))
print('random'.title().center(50))
np,tz,sa=strategie(SI)
print('#incercari:',np,', #tranz:',tz,', #sa:',sa)

