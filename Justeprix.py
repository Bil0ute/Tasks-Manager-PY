from random import randint

jpbib = {
        "d'une PS5": 500.0,
         "d'un manga": 7.0,
         "d'un ventilateur": 40.0,
         "d'un frigo": 600.0,
         "d'un bonbon": 0.20,
         "d'une bouteille d'eau": 0.50,
         "d'une paire basket Nike": 120.0,
         "d'un iphone 17": 1100.0,
         "d'un appartement à Paris de 70m²": 700000.0
        }


res = randint(0, len(jpbib)-1)
obj = (list(jpbib)[res])
prix = list(jpbib.values())[res]
print(f"Vous devez deviner le prix {obj}")

def s1():
    try:
        rep = float(input("Votre réponse (réponse décimal possible): "))
    except:
        print("Réponse non conforme, veillez re essayer")
        return s1()
    if rep != prix:
        if rep > prix:
            print("Moins cher !")
            return s1()
        elif rep < prix:
            print("Plus cher !")
            return s1()
    elif rep == prix:
        print("Bravo vous avez trouvé la bonne réponse !")


s1()
