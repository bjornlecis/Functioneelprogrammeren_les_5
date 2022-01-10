getal = 754752
getal = str(getal)
lengte = len(getal)

for i in range(lengte):
    hulp = int(getal[i])
    uitkomst = hulp*10**(lengte-1)
    print(uitkomst)
    lengte = lengte-1


