
def tranzitie(SC,piesa,tija):
    SC[piesa] = tija
    return SC

def st_finala(SC,SF):
    return SC == SF

def validare(SC,SA,piesa):
    SP = SA[:piesa]
    return not (SC[piesa] in SP or SA[piesa] in SP)


# SI = (1,)*4
# SF = (3,)*4
# print(st_finala((3,)*4))
# l = [1]*4
# print(l)
# print(SI == tuple(l))