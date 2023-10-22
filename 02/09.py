borya = int(input())
vova = int(input())
dima = int(input())
if vova > dima and vova > borya:
    max = vova
    if dima > borya:
        min = borya
        norm = dima
    else:
        min = dima
        norm = borya
elif dima > vova and dima > borya:
    max = dima
    if vova > borya:
        min = borya
        norm = vova
    else:
        min = vova
        norm = borya
else:
    max = borya
    if dima > vova:
        min = vova
        norm = dima
    else: 
        min = dima
        norm = vova
print(max, norm, min)
