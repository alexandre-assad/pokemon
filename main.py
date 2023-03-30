from pokemon import *
from type import *
import random
import pygame 



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
            self.pokemon2.setVie(self.pokemon2.getVie()-(((((self.pokemon1.lvl*0.4+2)*self.pokemon1.atk*int(self.pokemon1.competence[indexcompetence].degat))/self.pokemon2.deff)/50)+2)*self.pokemon1.type.howEffective(self.pokemon2.type.type))
        else:
            self.pokemon1.setVie(self.pokemon1.getVie()-(((((self.pokemon2.lvl*0.4+2)*self.pokemon2.atk*int(self.pokemon2.competence[indexcompetence].degat))/self.pokemon1.deff)/50)+2)*self.pokemon2.type.howEffective(self.pokemon1.type.type))

    def draw(self,n):
        if n == 0:
            screen.blit(self.pokemon1.img, (self.pokemon1.x, self.pokemon1.y))
        else:
            screen.blit(self.pokemon2.img, (self.pokemon2.x, self.pokemon2.y))
    
    def showInfo(self):
        print(self.pokemon1,"\n",self.pokemon2)
        
        
#Les Pokemons 
ouisticramPng = pygame.image.load("ouisticram.png")
ouisticramPng1 = pygame.image.load("ouisticram1.png")
ouisticramPng1 = pygame.transform.scale(ouisticramPng1,(250,250))
Ouisticram = Pokemon("Ouisticram",Type(List_type.Feu),ouisticramPng,pv=229,atk=152,defense=124)
Ouisticram.getCompetence()
bulbizarrePng = pygame.image.load("bulbizarre.png")
bulbizarrePng1 = pygame.image.load("bulbizarre1.png")
Bulbizarre = Pokemon("Bulbizarre",Type(List_type.Plante),bulbizarrePng,pv=231,atk=166,defense=166)
Bulbizarre.getCompetence()


#Dimoret = Pokemon("Dimoret",Type([List_type.Glace,List_type.Tenebre]))
#Dimoret.getCompetence()

class Cadre:
    def __init__(self,img,x,y,pokemon):
        self.img = img
        self.x = x
        self.y = y
        self.pokemon = pokemon
        self.index = 0
        
    def drawPokemon(self):
        screen.blit(self.img,(self.x,self.y))
        pokeName = font.render(str(self.pokemon.getName()),True,(5,5,5))
        pokeVie = font.render("PV : "+str(round(self.pokemon.getVie())),True,(5,5,5))
        screen.blit(pokeName,(self.x+50,self.y+20))
        screen.blit(pokeVie,(self.x+50,self.y+50))
        
    def drawText(self):
        screen.blit(self.img,(self.x,self.y))
        attaque = []
        for i in range(4):
            if i == self.index:
                attaque.append(capacityFont.render(str(self.pokemon.competence[i].nom),True,(255,10,10)))
            else:
                attaque.append(capacityFont.render(str(self.pokemon.competence[i].nom),True,(10,10,10)))
        screen.blit(attaque[0],(self.x+50,self.y+40))
        screen.blit(attaque[1],(self.x+200,self.y+40))
        screen.blit(attaque[2],(self.x+50,self.y+70))
        screen.blit(attaque[3],(self.x+200,self.y+70))
        
    def getIndex(self):
        global run
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN :
                if self.index == 3 or self.index == 1:
                    if event.key == pygame.K_LEFT:
                        self.index -=1
                elif self.index == 0 or self.index == 2:
                    if event.key == pygame.K_RIGHT:
                        self.index +=1
                if self.index == 0 or self.index == 1:
                    if event.key == pygame.K_DOWN:
                        self.index +=2
                elif self.index == 2 or self.index == 3:
                    if event.key == pygame.K_UP:
                        self.index -= 2
                if event.key == pygame.K_a:
                    print("hey") 
                    partie.attaque(0,self.index)
                    if partie.verifieFin():
                        run = False
                        return True  
                    partie.attaque(1,random.randint(0,3))
                    if partie.verifieFin():
                        run = False
                        return True
    

partie = Combat(Bulbizarre,Ouisticram)
Bulbizarre.x =180
Bulbizarre.y = 220
Bulbizarre.img = pygame.image.load("bulbizarre1.png")
Ouisticram.x = 550
Ouisticram.y = 140
pygame.init()

screen = pygame.display.set_mode((1050,540))
background = pygame.image.load('background_pokemon.jpg')
pygame.display.set_caption("Combat Pokemon")
font = pygame.font.Font('freesansbold.ttf',15)
capacityFont = pygame.font.Font('freesansbold.ttf',20)
cadreImg = pygame.image.load("cadreText.png")
cadrePokemonImg = pygame.image.load("cadrePokemon.png")
cadrePokemonImg2 = pygame.image.load("cadrePokemon2.png")
cadreText = Cadre(cadreImg,0,390,partie.pokemon1)
cadrePokemon = Cadre(cadrePokemonImg,50,100,partie.pokemon1)
cadrePokemon2 = Cadre(cadrePokemonImg2,700,290,partie.pokemon2)
run = True
while run:
    screen.fill((35,35,35))
    screen.blit(background, (0,0))
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
    partie.draw(0)
    partie.draw(1)
    cadreText.drawText()
    cadreText.getIndex()
    cadrePokemon.drawPokemon()
    cadrePokemon2.drawPokemon()
    
    pygame.display.update()
pygame.quit()


# game = input("(1)Lancer une partie\n")
# if game == "1":
#     while run:
#         action = input(f"""                       
# (1) {partie.pokemon1.competence[0].nom} / {partie.pokemon1.competence[0].degat}
# (2) {partie.pokemon1.competence[1].nom} / {partie.pokemon1.competence[1].degat}
# (3) {partie.pokemon1.competence[2].nom} / {partie.pokemon1.competence[2].degat}
# (4) {partie.pokemon1.competence[3].nom} / {partie.pokemon1.competence[3].degat}
# """)
#         if action == "1":
#             partie.attaque(0,0)
#             print("Vous avez Attaqué")
#             if partie.verifieFin():
#                 break
#             partie.attaque(1,random.randint(0,3))
#             print("Il vous a attaqué")
#             if partie.verifieFin():
#                 break
#         elif action == "2":
#             partie.attaque(0,1)
#             print("Vous avez Attaqué")
#             if partie.verifieFin():
#                 break
#             partie.attaque(1,random.randint(0,3))
#             print("Il vous a attaqué")
#             if partie.verifieFin():
#                 break
#         elif action == "3":
#             partie.attaque(0,2)
#             print("Vous avez Attaqué")
#             if partie.verifieFin():
#                 break
#             partie.attaque(1,random.randint(0,3))
#             print("Il vous a attaqué")
#             if partie.verifieFin():
#                 break
#         elif action == "4":
#             partie.attaque(0,3)
#             print("Vous avez Attaqué")
#             if partie.verifieFin():
#                 break
#             partie.attaque(1,random.randint(0,3))
#             print("Il vous a attaqué")
#             if partie.verifieFin():
#                 break
#         else:
#             print("Veuillez attaquer")
#         partie.showInfo()
        