def maak_koffie_op_nummer(keuze):
    hulp = 0
    koffie = "Koffie bestaat uit"
    if(keuze>8):
        koffie = koffie,"Extra straf + "
        hulp = keuze-8
        keuze = keuze - hulp
    elif(keuze >4):
        koffie = koffie,"Melk + "
        hulp = keuze-4
        keuze = keuze - hulp
    elif(keuze >2):
        koffie = koffie,"Suiker + "
        hulp = keuze-2
        keuze = keuze - hulp
    elif(keuze >1):
        koffie = koffie,"Koekje + "
    print(koffie)



keuze = int(input("geef een waarde in"))
maak_koffie_op_nummer(keuze)

