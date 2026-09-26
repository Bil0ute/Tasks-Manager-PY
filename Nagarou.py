import flet as ft
import random
from random import shuffle

def main(page: ft.Page):
    page.scroll = ft.ScrollMode.AUTO

    note = ft.TextField(
        label="Notes du narrateur",
        multiline=True,
        min_lines=3,
        max_lines=10,)

    ln =[]
    nap = ft.Text("\n \nNagarou")
    prs = ft.Text("Bienvenue sur Nagarou cher Narrateur ! \n"
                  "Combien de personne participe à la partie ?")
    CPJ = ft.Text("0")
    compteur_roles = ft.Text("0 rôle(s) coché(s)")

    def pnbj():
        CPJ.value = int(CPJ.value) + 1
        page.update()

    def mnbj():
        CPJ.value = int(CPJ.value) - 1
        if CPJ.value < 0:
            CPJ.value = 0
        page.update()

    roles = [
        "Simple villageois",
        "Chasseur",
        "Voyante",
        "Petite fille",
        "Sorcière",
        "Garde/Salvateur",
        "Corbeau",
        "chien-Loup",
        "Enfant Sauvage",
        "Oracle",
        "Ancien",
        "Renard",
        "Montreur d'ours",
        "Soeur 1",
        "Soeur 2",
        "Idiot du Village",
        "Cupidon",
        "Assasin",
        "Pyromane",
        "Joueur de flûte",
        "Mouton",
        "Ange",
        "Voleur",
        "Loup Garou 1",
        "Loup Garou 2",
        "Loup Garou Blanc",
        "Infect père des loups",
        "Loup Garou Maudit",
        "Grand Méchant Loup"

    ]

    def cpc():
        total = 0
        total = sum(1 for cb in checkboxes_roles if cb.value)
        compteur_roles.value = f"{total} rôle(s) coché(s) sur {CPJ.value}"

    checkboxes_roles = [ft.Checkbox(label=x, on_change=cpc) for x in roles]
    drop_etat = []
    drop_etat2 = []
    plt = []

    async def explication(e):
        await page.launch_url("https://loupgarou.fandom.com/fr/wiki/Liste_des_r%C3%B4les")

    def notes():
        page.controls.clear()
        page.add(ft.Text("\n \n📝 Notes", size=20, weight=ft.FontWeight.BOLD))
        page.add(note)
        page.add(ft.Button("Retour", on_click=pg))
        page.update()

    def ordre():
        page.controls.clear()
        page.add(ft.Text("\n \n🌙 Nuit 1 (avec Cupidon)\n1.Cupidon \n2.couple(reconnaissance) \n3.Enfant Sauvage(choisis son mentor) \n4.Sœurs (reconnaissance) \n5.Chien Loup (choisis son camp) \n6.Voleur(choisis sa carte parmi les 2 proposé) \n7.Loups-Garous (reconnaissance de la meute) \n8.Fin de nuit normale \n\n🌙 Nuits suivantes \n1.Garde / Salvateur \n2.Voyante \n3.Oracle \n4.Renard \n5.Joueur de Flûte \n6.Pyromane \n7.Assassin \n8.Loups-Garous (choix de la victime) \n9.Grand Méchant Loup (choisit éventuellement une seconde victime) \n10.Infect Père des Loups (décide d'infecter ou non) \n11.Loup Maudit (décide de maudire ou non la victime principale) \n12.Loup-Garou Blanc (une nuit sur deux) \n13.Corbeau \n14.Sorciere \n15.Lever du jour \n\n\nNote pour le Mouton: \nAprès toutes les attaques : \nSi le Mouton est ciblé pour la première fois : \n→ il survit \n→ rejoint le camp responsable \nSi le Mouton est déjà converti : \n→ il meurt normalement \n\nNe pas oublier l'Enfant Sauvage si son mentor meurt \nBien noter les victimes du pyromane et du joueur de flûte \n Ne pasoublier le joueur maudit si il y en a un", size = 15))
        page.add(ft.Button("Retour", on_click=pg))
        page.update()

    def pg():
        page.controls.clear()
        page.add(ft.Text("\n \nVoici la page principal de la partie cher Narrateur !"))
        liste = ["Mort", "Vivant", "Couple"]
        liste2 = ["Ensorcellé(e)", "Odeur d'essence","Les deux", "Rien"]
        if not drop_etat and not drop_etat2:
            for nj, role in liste_prt.items():
                rp = ft.Dropdown(
                    label=f"{nj} ({role})",
                    options=[ft.dropdown.Option(etat) for etat in liste],
                    value="Vivant"
                )

                rp2 = ft.Dropdown(
                    label=f"{nj} ({role})",
                    options=[ft.dropdown.Option(etat) for etat in liste2],
                    value="Rien"
                )
                drop_etat.append(rp)
                drop_etat2.append(rp2)
        if not plt:
            cpt = ft.Dropdown(
                label = "Qui est Maire du Village ?",
                options = [ft.dropdown.Option(J.value) for J in ln]
            )
            plt.append(cpt)

        for rp, rp2 in zip(drop_etat, drop_etat2):
            page.add(ft.Row([
                (rp),
                (rp2)
            ]))
        page.add(plt[0])

        page.add(ft.Button("Explication des rôles", on_click = explication))
        page.add(ft.Button("Ordre d'appel", on_click = ordre))
        page.add(ft.Button("Note du Narrateur", on_click=notes))
        page.update()




    liste_prt = {}
    drop = []

    def définir():
        page.controls.clear()
        page.add(ft.Text("\n \nDéfinissez l'attribution de vos rôles !"))
        roles_coches = [cb.label for cb in checkboxes_roles if cb.value]
        for x in ln:
            nj = x.value
            dropdown = ft.Dropdown(
                label = nj,
                options = [ft.dropdown.Option(role) for role in roles_coches]
            )
            page.add(dropdown)
            drop.append(dropdown)

        def valider():
            for x, y in zip(ln, drop):
                liste_prt[x.value] = y.value
            pg()


        page.add(ft.Button("Valider", on_click=valider))
        page.add(ft.Button("Retour", on_click=p))
        page.update()



    def rdm():
        page.controls.clear()
        page.add(ft.Text("\n \n Voici l'attribution des rôles"))
        roles_coches = [cb.label for cb in checkboxes_roles if cb.value]
        random.shuffle(roles_coches)
        for x, y in zip(ln, roles_coches):
            liste_prt[x.value] = y
        for nj, role in liste_prt.items():
            page.add(ft.Text(f"{nj} : {role}"))
        page.add(ft.Button("Retour", on_click=p))
        page.add(ft.Button("Continuer", on_click=pg))
        page.update()

    def p():
        page.controls.clear()
        page.add(ft.Text("\n \nSouhaitez vous que les rôles soient attribuer aléatoirement ou preferez vous définir les rôles vous mêmes ?"))
        page.add(ft.Row([ft.Button("Aléatoire", on_click = rdm), ft.Button("Définir", on_click = définir)]))
        page.add(ft.Button("Retour", on_click=PP))


    def lcp():
        page.controls.clear()
        page.add(ft.Text("\n \n Qui jouera ?"))
        for i in range (int(CPJ.value)):
            nom = ft.TextField(label = f"Entrer le nom du joueur {i+1}")
            ln.append(nom)
            page.add(nom)
        page.add(ft.Button("Continuer", on_click=p))
        page.add(ft.Button("Retour", on_click=PP))
        page.update()



    def PR():
        page.controls.clear()
        page.add(ft.Text("\n \n Voici la liste des rôles !"))
        page.add(ft.Button("Retour", on_click=PP))
        for cb in checkboxes_roles:
            page.add(cb)
        page.add(compteur_roles)
        page.add(ft.Text("Attention: choisissez bien le même nombre de rôle(s) que de joueur(s)"))
        page.update()


    def PP():
        page.controls.clear()
        ln.clear()
        page.add(nap)
        page.add(prs)
        page.add(CPJ)
        page.add(ft.Row([
            ft.Button("Augmenter", on_click=pnbj),
            ft.Button("Baisser", on_click=mnbj),
        ]))
        page.add(ft.Button("Rôles", on_click=PR))
        page.add(ft.Button("Lancer la partie", on_click=lcp))
        page.update()

    PP()


ft.run(main)
