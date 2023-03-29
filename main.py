from pokemon import *
from type import *
import random

class Combat:
    
    def __init__(self,pokemon1,pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        
    def vainqueur(self):
        if self.pokemon1.getVie() <= 0:
            return [str(self.pokemon2.getName()),str(self.pokemon1.getName())]
        elif self.pokemon2.getVie() <= 0:
            return [str(self.pokemon1.getName()),str(self.pokemon2.getName())]
        
    def verifieFin(self):
        if self.pokemon1.getVie() <= 0 or self.pokemon2.getVie() <= 0:
            print(f"Le Pokemon {self.vainqueur()[0]} a gagne !\nLe Pokemon {self.vainqueur()[1]} a perdu ...")
            return True
        else:
            return False
            
    def attaque(self,tour,indexcompetence):
        if tour == 0:
            self.pokemon2.setVie(self.pokemon2.getVie()-(((((self.pokemon1.lvl*0.4+2)*self.pokemon1.atk*int(self.pokemon1.competence[indexcompetence].degat))/self.pokemon2.deff)/50)+2)*random.uniform(0.8,1.2)*self.pokemon1.type.howEffective(self.pokemon2.type.type))
        else:
            self.pokemon1.setVie(self.pokemon1.getVie()-(((((self.pokemon2.lvl*0.4+2)*self.pokemon2.atk*int(self.pokemon2.competence[indexcompetence].degat))/self.pokemon1.deff)/50)+2)*random.uniform(0.8,1.2)*self.pokemon2.type.howEffective(self.pokemon1.type.type))

    
    
    def showInfo(self):
        print(self.pokemon1,"\n",self.pokemon2)
        
    
Ouisticram = Pokemon("Ouisticram",Type(List_type.Feu))
Herbizarre = Pokemon("Herbizarre",Type(List_type.Plante))
Herbizarre.getCompetence()
Ouisticram.getCompetence()

Dimoret = Pokemon("Dimoret",Type([List_type.Glace,List_type.Tenebre]))
Dimoret.getCompetence()
partie = Combat(Dimoret,Herbizarre)
run = True
game = input("(1)Lancer une partie\n")
if game == "1":
    while run:
        action = input(f"""                       
(1) {partie.pokemon1.competence[0].nom} / {partie.pokemon1.competence[0].degat}
(2) {partie.pokemon1.competence[1].nom} / {partie.pokemon1.competence[1].degat}
(3) {partie.pokemon1.competence[2].nom} / {partie.pokemon1.competence[2].degat}
(4) {partie.pokemon1.competence[3].nom} / {partie.pokemon1.competence[3].degat}
""")
        if action == "1":
            partie.attaque(0,0)
            print("Vous avez Attaqué")
            if partie.verifieFin():
                break
            partie.attaque(1,random.randint(0,3))
            print("Il vous a attaqué")
            if partie.verifieFin():
                break
        elif action == "2":
            partie.attaque(0,1)
            print("Vous avez Attaqué")
            if partie.verifieFin():
                break
            partie.attaque(1,random.randint(0,3))
            print("Il vous a attaqué")
            if partie.verifieFin():
                break
        elif action == "3":
            partie.attaque(0,2)
            print("Vous avez Attaqué")
            if partie.verifieFin():
                break
            partie.attaque(1,random.randint(0,3))
            print("Il vous a attaqué")
            if partie.verifieFin():
                break
        elif action == "4":
            partie.attaque(0,3)
            print("Vous avez Attaqué")
            if partie.verifieFin():
                break
            partie.attaque(1,random.randint(0,3))
            print("Il vous a attaqué")
            if partie.verifieFin():
                break
        else:
            print("Veuillez attaquer")
        partie.showInfo()
        