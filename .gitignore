def presentation():
    print("Bienvenue dans le menu des Tâches \n"
        "Voici les options disponnibles: \n"
        " 1: Ajouter une tâche à votre liste \n"
        " 2: Supprimer une tâche de votre liste \n"  
        " 3: Afficher la liste des tâches \n"
        " 4: Regarder quelle tâche sont validées ou non\n"
        " 5: Valider ou invalider les tâches souhaitées\n"
        " 6: Quitter")

def menu():
        presentation()
        try:
            res = int(input("Choix: "))
            if 0 > res or res > 6:
                print("choix invalide")
                return menu()
            return res
        except:
            print("choix invalide")
            return menu()


import json

def charger():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except:
        return []

def sauvegarder(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)


tasks = charger()
res = menu()

while res != 6:
    if res == 1:
        nom = input("Nom de la tâche: ")
        NT = {"nom": nom,
              "faite": False}
        tasks.append(NT)
        sauvegarder(tasks)
        print("Tâche ajoutée")
        res = menu()

    elif res == 3:
        if not tasks:
            print("Aucune tâche pour le moment")
        else:
            for i in range (len(tasks)):
                print(i, "-", tasks[i]["nom"])
        res = menu()

    elif res == 2:
        if not tasks:
            print("Aucune tâche pour le moment")
        else:
            for i in range (len(tasks)):
                print(i, "-", tasks[i]["nom"], "-", tasks[i]["faite"])
            idx = (int(input("Quel élément souhaitez vous supprimer (le 1er élément est noté 0)")))
            if 0 <= idx < len(tasks):
                cfrm = input("êtes vous sûr ? (oui/non)")
                if cfrm == "oui":
                    print(tasks[idx]["nom"], "supprimé avec succés !")
                    tasks.pop(idx)
                    sauvegarder(tasks)
                elif cfrm == "non":
                    print("retour au menu")
                    res = menu()
                else:
                    print("INVALIDE")
                    res = menu()
            else:
                print("Erreur valeur non disponnible")
        res = menu()

    elif res == 4:
        if not tasks:
            print("Aucune tâche pour le moment")
        else:
            vld = input("Souhaitez vous voir les tâches validées ou non validées ? (oui/non) ")
            if vld == "oui":
                for i in range (len(tasks)):
                    if tasks[i]["faite"] == True:
                        print(i, "-", tasks[i]["nom"])
                res = menu()
            elif vld == "non":
                for i in range (len(tasks)):
                    if tasks[i]["faite"] == False:
                        print(i, "-", tasks[i]["nom"])
                res = menu()
            else:
                print("Erreur")
                res = menu()

    elif res == 5:
        if not tasks:
            print("Aucune tâche pour le moment")
        else:
            for i in range (len(tasks)):
                print(i, "-", tasks[i]["nom"], "-", tasks[i]["faite"])
            idf = int(input("Quelle tâche souhaitez vous valider/invalider ? (le 1er élément est noté 0) "))
            if 0 <= idf < len(tasks):
                if tasks[idf]["faite"] == True:
                    tasks[idf]["faite"] = False
                    print("Element invalidé !")
                elif tasks[idf]["faite"] == False:
                     tasks[idf]["faite"] = True
                     print("Element validé !")
                sauvegarder(tasks)
                res = menu()
            else:
                print("Erreur valeur non trouvé")
                res = menu()

    else:
        print("INVALIDE")
        res = menu()

print("Bonne journée !")
