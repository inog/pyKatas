noten = [1,1,2,5,5,6]

for i in range(len(noten)):
    print(noten[i])

print("\n")

fächer=["Mathe","Deutsch","Englisch","Sport","Kunst","Informatik"]

for note, fach in zip(noten,fächer):
    print(note, " - ",fach)

print("\n")

präferenzen=["Mathe","Deutsch","Englisch","Sport","Kunst","Informatik"]

for index, fach in enumerate(präferenzen):
    print("Das Fach: ",fach, "ist an Stelle: ", index+1)