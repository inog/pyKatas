binIchReich = None
binIchPleite = None

kontostand = 0

if kontostand > 0:
    binIchPleite = False
elif kontostand == 0:
    print("Mies gelaufen")
else:
    binIchPleite = True
    binIchReich = False