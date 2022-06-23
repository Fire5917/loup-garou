#By Fire5917
import time
import colorama
import random
joueurs = []
loups = []
nbr_de_joueurs = int(input("Combien de joueurs vont jouer? (min 4) >>>"))
if nbr_de_joueurs < 4:
    print("pas assez de joueurs...")
    input("Appuyez sur entrée pour quitter")
    exit()
for i in range(nbr_de_joueurs):
    for joueur in joueurs:
        print(joueur)
    nom_du_joueur = input("Quel est le nom du joueur? >>>")
    joueurs.append(nom_du_joueur)
colorama.init()
print(colorama.Fore.BLUE + "Joueurs inscrits :" + colorama.Fore.GREEN)
joueurs_en_vie = joueurs.copy()
nbr_de_loups = nbr_de_joueurs / 4
nbr_de_loups_1 = int(nbr_de_loups)
for joueur in joueurs:
    print(joueur)
for i in range(nbr_de_loups_1):
    joueur_random = random.choice(joueurs)
    loups.append(joueur_random)
    joueurs.pop(joueurs.index(joueur_random))
joueur_random = random.choice(joueurs)
cupidon = joueur_random
joueurs.pop(joueurs.index(joueur_random))
joueur_random = random.choice(joueurs)
chasseur = joueur_random
joueurs.pop(joueurs.index(joueur_random))
joueur_random = random.choice(joueurs)
sorciere = joueur_random
joueurs.pop(joueurs.index(joueur_random))
print(colorama.Fore.RED + "Les loups sont : ")
for loup in loups:
    print(loup)
print(colorama.Fore.MAGENTA + f"Cupidon est : {cupidon}")
print(colorama.Fore.LIGHTGREEN_EX + f"Le chasseur est : {chasseur}")
print(colorama.Fore.CYAN + f"La sorcière est : {sorciere}")
print(colorama.Fore.YELLOW + "Les villageois sont :")
for joueur in joueurs:
    print(joueur)
time.sleep(100.0)


