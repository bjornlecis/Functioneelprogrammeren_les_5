woord = "Januari"
lengte = len(woord)
lijst = []

# woord naar ascii
for i in range(lengte):
    lijst.append(ord(woord[i]))

print(lijst)

#ascii naar woord
for j in range(lengte):
   print(chr(lijst[j]))
