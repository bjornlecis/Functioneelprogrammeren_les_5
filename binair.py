getal = 1011
getal = str(getal)
lengte = len(getal)

som = 0
for i in range(lengte):
    hulp = int(getal[i])
    uitkomst = hulp*2**(lengte-1)
    print(uitkomst)
    lengte = lengte-1
    som = som + uitkomst

print(som)

