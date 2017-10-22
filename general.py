
def piesa_urmatoare(SC,m,n):
    i = 0
    for j in range(2, m + 1):
        if SC[j:] == [n] * (m - j + 1):
            i = j
            break
    return i

def tranzitie(SC,piesa,tija):
    SC[piesa] = tija
    return SC

def st_finala(SC,SF):
    return SC == SF

def validare(SC,SA,piesa):
    SP = SA[1:piesa]
    return (not ((SC[piesa] in SP) or (SA[piesa] in SP)))


# SI = (1,)*4
# SF = (3,)*4
# print(st_finala((3,)*4))
# l = [1]*4
# print(l)
# print(SI == tuple(l))

# piesa 3 tija 3
# 2 1 1
# 2 1 3

# 1 1 1
# 1 1 3
# 1 3 3
# 3 3 3

# 3 2 3 -> 3 3 3
