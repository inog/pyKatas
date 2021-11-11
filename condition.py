rich = None
poor = None

bankaccount = 123

if bankaccount > 0:
    poor = False
    print("OK !")
elif bankaccount == 0:
    poor = True
    print("Shit happens")
else:
    poor = True
    rich = False
    print("There is something to do.")

