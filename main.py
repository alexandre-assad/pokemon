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
            
    def attaque(self,tour):
        if tour == 0:
            self.pokemon2.setVie(self.pokemon2.getVie()-(((((self.pokemon1.lvl*0.4+2)*self.pokemon1.atk*100)/self.pokemon2.deff)/50)+2)*random.uniform(0.8,1.2)*self.pokemon1.type.howEffective(self.pokemon2.type.type))
            self.pokemon1.setVie(self.pokemon1.getVie()-(((((self.pokemon2.lvl*0.4+2)*self.pokemon2.atk*100)/self.pokemon1.deff)/50)+2)*random.uniform(0.8,1.2)*self.pokemon2.type.howEffective(self.pokemon1.type.type))

    
    
    def showInfo(self):
        print(self.pokemon1,"\n",self.pokemon2)
        
    
Ouisticram = Pokemon("Ouisticram",Type(List_type.Feu))
Herbizarre = Pokemon("Herbizarre",Type(List_type.Plante))
Dimoret = Pokemon("Dimoret",Type([List_type.Glace,List_type.Tenebre]))
partie = Combat(Dimoret,Herbizarre)
run = True
game = input("(1)Lancer une partie\n")
if game == "1":
    while run:
        action = input("""                       
(1) Attaquer
""")
        if action == "1":
            partie.attaque(0)
            print("Vous avez Attaqué")
            if partie.verifieFin():
                
                break
            partie.attaque(1)
            print("Il vous a attaqué")
            if partie.verifieFin():
                break
        else:
            print("Veuillez attaquer")
        partie.showInfo()
        