#By Fire5917 & Frigogel
import time
import colorama
import random
colorama.init()
def lines(x):
    print(colorama.Fore.YELLOW + "=========================" + colorama.Fore.WHITE)
joueurs = []
loups = []
regle = input("Voulez vous savoir les règles? (y/n) >>> ")
if regle == "y":
    print(colorama.Fore.GREEN + """
________                ______              
___  __ \_____ _______ ____  /_____ ________
__  /_/ /_  _ \__  __ `/__  / _  _ \__  ___/
_  _, _/ /  __/_  /_/ / _  /  /  __/_(__  ) 
/_/ |_|  \___/ _\__, /  /_/   \___/ /____/  
               /____/                           
    """)
    print(colorama.Fore.CYAN + "Voci les différents rôles : ")
    time.sleep(1.0)
    lines(1)
    print(colorama.Fore.LIGHTBLUE_EX + "Le villageois : ")
    print(colorama.Fore.BLUE + "Son objectif est d'éliminer tous les Loups-Garous. Il ne dispose d'aucun pouvoir particulier : uniquement sa perspicacité et sa force de persuasion.")
    lines(1)
    input("appuyez sur entrée pour continuer")
    lines(1)
    print(colorama.Fore.RED + "Le loup garou : ")
    print(colorama.Fore.BLUE + "Son objectif est d'éliminer tous les innocents (ceux qui ne sont pas Loups-Garous). Chaque nuit, il se réunit avec ses compères Loups pour décider d'une victime à éliminer...")
    lines(1)
    input("appuyez sur entrée pour continuer")
    lines(1)
    print(colorama.Fore.LIGHTRED_EX + "La sorcière : ")
    print(colorama.Fore.BLUE + "Son objectif est d'éliminer tous les Loups-Garous. Elle dispose de deux potions : une potion de vie pour sauver la victime des Loups, et une potion de mort pour assassiner quelqu'un.")
    lines(1)
    input("appuyez sur entrée pour continuer")
    lines(1)
    print(colorama.Fore.MAGENTA + "Cupidon : ")
    print(colorama.Fore.BLUE + "Son objectif est d'éliminer tous les Loups-Garous. Dès le début de la partie, il doit former un couple de deux joueurs. Leur objectif sera de survivre ensemble, car si l'un d'eux meurt, l'autre se suicidera.")
    lines(1)
    input("appuyez sur entrée pour continuer")
    lines(1)
    print(colorama.Fore.GREEN + "Le chasseur :")
    print(colorama.Fore.BLUE + "Son objectif est d'éliminer tous les Loups-Garous. A sa mort, il doit éliminer un joueur en utilisant sa dernière balle...")
    lines(1)

try:
    nbr_de_joueurs = int(input("Combien de joueurs vont jouer? (min 6) >>>"))
except ValueError:
    print(colorama.Fore.RED + "[!] Veuillez mettre un chiffre !")
    nbr_de_joueurs = int(input("Combien de joueurs vont jouer? (min 6) >>>"))
if nbr_de_joueurs < 6:
    print("pas assez de joueurs...")
    input("Appuyez sur entrée pour quitter")
    exit()

for i in range(nbr_de_joueurs):
    for joueur in joueurs:
        print(joueur)
    nom_du_joueur = input("Quel est le nom du joueur? >>>")
    joueurs.append(nom_du_joueur)
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


