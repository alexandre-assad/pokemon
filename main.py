from pokemon import *
from type import *
import random
import pygame 



class Combat:
    
    def __init__(self,pokemon1,pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        
        
    def verifieFin(self):
        if self.pokemon1.getVie() <= 0:
            self.pokemon1.etat = "mort"
        if self.pokemon1.etat == "mort":
            for i in Team:
                if i.etat == "vie":
                    self.pokemon1 = i
                    self.pokemon1.x =160
                    self.pokemon1.y = 220
                    return "Changement"
            print("Defaite")
            return "Defaite"
        
        if self.pokemon2.getVie() <= 0:
            self.pokemon2.etat = "mort"
        if self.pokemon2.etat == "mort":
            for i in TeamEnemy:
                if i.etat == "vie":
                    self.pokemon2 = i
                    self.pokemon2.x = 550
                    self.pokemon2.y = 90
                    return True
            print("Victoire")
            return "Victoire"
        
                    
                    
    def attaque(self,tour,indexcompetence):
        if tour == 0:
            self.pokemon2.setVie(self.pokemon2.getVie()-(((((self.pokemon1.lvl*0.4+2)*self.pokemon1.atk*int(self.pokemon1.competence[indexcompetence].degat))/self.pokemon2.deff)/50)+2)*Type(self.pokemon1.competence[indexcompetence].type).howEffective(self.pokemon2.type.type))
        else:
            self.pokemon1.setVie(self.pokemon1.getVie()-(((((self.pokemon2.lvl*0.4+2)*self.pokemon2.atk*int(self.pokemon2.competence[indexcompetence].degat))/self.pokemon1.deff)/50)+2)*Type(self.pokemon2.competence[indexcompetence].type).howEffective(self.pokemon1.type.type))

    def draw(self,n):
        if n == 0:
            screen.blit(self.pokemon1.img, (self.pokemon1.x, self.pokemon1.y))
        else:
            screen.blit(self.pokemon2.img, (self.pokemon2.x, self.pokemon2.y))
    
    def showInfo(self):
        print(self.pokemon1,"\n",self.pokemon2)
        
   
#Les Pokemons 
dimoretPng = pygame.image.load("dimoret.png")
dimoretIcon = dimoretPng
dimoretPng = pygame.transform.scale(dimoretPng,(250,250))
dimoretPng1 = pygame.image.load("dimoret1.png")
dimoretPng1 = pygame.transform.scale(dimoretPng1,(250,250))
Dimoret = Pokemon("Dimoret",Type([List_type.Glace,List_type.Tenebre]),[dimoretPng,dimoretPng1],pv=281,atk=276,defense=206)
Dimoret.getCompetence()

#Poke test 
P1 = Pokemon("a",Type(List_type.Normal),[dimoretPng,dimoretPng1],pv=281,atk=276,defense=206)    
P2 = Pokemon("a",Type(List_type.Normal),[dimoretPng,dimoretPng1],pv=281,atk=276,defense=206)    
lucarioPng = pygame.image.load("lucario.png")
LucarioIcon = lucarioPng
lucarioPng = pygame.transform.scale(lucarioPng,(250,250))
lucarioPng1 = pygame.image.load("lucario1.png")
lucarioPng1 = pygame.transform.scale(lucarioPng1,(250,250))
Lucario = Pokemon("Lucario",Type([List_type.Combat,List_type.Acier]),[lucarioPng,lucarioPng1],pv=281,atk=266,defense=176)
Lucario.getCompetence()

PingoleonPng = pygame.image.load("pingoleon.png")
PingoleonIcon = PingoleonPng
PingoleonPng = pygame.transform.scale(PingoleonPng,(250,250))
PingoleonPng1 = pygame.image.load("pingoleon1.png")
PingoleonPng1 = pygame.transform.scale(PingoleonPng1,(250,250))
Pingoleon = Pokemon("Pingoleon",Type([List_type.Eau,List_type.Acier]),[PingoleonPng,PingoleonPng1],pv=309,atk=258,defense=238)
Pingoleon.getCompetence()

SimiabrazPng = pygame.image.load("Simiabraz.png")
SimiabrazIcon = SimiabrazPng
SimiabrazPng = pygame.transform.scale(SimiabrazPng,(250,250))
SimiabrazPng1 = pygame.image.load("Simiabraz1.png")
SimiabrazPng1 = pygame.transform.scale(SimiabrazPng1,(250,250))
Simiabraz = Pokemon("Simiabraz",Type([List_type.Combat,List_type.Feu]),[SimiabrazPng,SimiabrazPng1],pv=293,atk=244,defense=178)
Simiabraz.getCompetence()

MackogneurPng = pygame.image.load("Mackogneur.png")
MackogneurIcon = MackogneurPng
MackogneurPng = pygame.transform.scale(MackogneurPng,(250,250))
MackogneurPng1 = pygame.image.load("Mackogneur1.png")
MackogneurPng1 = pygame.transform.scale(MackogneurPng1,(250,250))
Mackogneur = Pokemon("Mackogneur",Type(List_type.Combat),[MackogneurPng,MackogneurPng1],pv=321,atk=296,defense=206)
Mackogneur.getCompetence()

ScorvolPng = pygame.image.load("Scorvol.png")
ScorvolIcon = ScorvolPng
ScorvolPng = pygame.transform.scale(ScorvolPng,(250,250))
ScorvolPng1 = pygame.image.load("Scorvol1.png")
ScorvolPng1 = pygame.transform.scale(ScorvolPng1,(250,250))
Scorvol = Pokemon("Scorvol",Type([List_type.Sol,List_type.Vol]),[ScorvolPng,ScorvolPng1],pv=291,atk=226,defense=286)
Scorvol.getCompetence()

LeviatorPng = pygame.image.load("Leviator.png")
LeviatorIcon = LeviatorPng
LeviatorPng = pygame.transform.scale(LeviatorPng,(250,250))
LeviatorPng1 = pygame.image.load("Leviator1.png")
LeviatorPng1 = pygame.transform.scale(LeviatorPng1,(250,250))
Leviator = Pokemon("Leviator",Type([List_type.Eau,List_type.Vol]),[LeviatorPng,LeviatorPng1],pv=331,atk=286,defense=236)
Leviator.getCompetence()

CizayoxPng = pygame.image.load("Cizayox.png")
CizayoxIcon = CizayoxPng
CizayoxPng = pygame.transform.scale(CizayoxPng,(250,250))
CizayoxPng1 = pygame.image.load("Cizayox1.png")
CizayoxPng1 = pygame.transform.scale(CizayoxPng1,(250,250))
Cizayox = Pokemon("Cizayox",Type([List_type.Insecte,List_type.Acier]),[CizayoxPng,CizayoxPng1],pv=281,atk=296,defense=236)
Cizayox.getCompetence()

ElechtorPng = pygame.image.load("Elechtor.png")
ElechtorIcon = ElechtorPng
ElechtorPng = pygame.transform.scale(ElechtorPng,(250,250))
ElechtorPng1 = pygame.image.load("Elechtor1.png")
ElechtorPng1 = pygame.transform.scale(ElechtorPng1,(250,250))
Elechtor = Pokemon("Elechtor",Type([List_type.Electrique,List_type.Vol]),[ElechtorPng,ElechtorPng1],pv=321,atk=286,defense=216)
Elechtor.getCompetence()

LeuphoriePng = pygame.image.load("Leuphorie.png")
LeuphorieIcon = LeuphoriePng
LeuphoriePng = pygame.transform.scale(LeuphoriePng,(250,250))
LeuphoriePng1 = pygame.image.load("Leuphorie1.png")
LeuphoriePng1 = pygame.transform.scale(LeuphoriePng1,(250,250))
Leuphorie = Pokemon("Leuphorie",Type(List_type.Normal),[LeuphoriePng,LeuphoriePng1],pv=651,atk=186,defense=306)
Leuphorie.getCompetence()

EctoplasmaPng = pygame.image.load("Ectoplasma.png")
EctoplasmaIcon = EctoplasmaPng
EctoplasmaPng = pygame.transform.scale(EctoplasmaPng,(250,250))
EctoplasmaPng1 = pygame.image.load("Ectoplasma1.png")
EctoplasmaPng1 = pygame.transform.scale(EctoplasmaPng1,(250,250))
Ectoplasma = Pokemon("Ectoplasma",Type([List_type.Spectre,List_type.Poison]),[EctoplasmaPng,EctoplasmaPng1],pv=261,atk=296,defense=186)
Ectoplasma.getCompetence()

JirachiPng = pygame.image.load("Jirachi.png")
JirachiIcon = JirachiPng
JirachiPng = pygame.transform.scale(JirachiPng,(250,250))
JirachiPng1 = pygame.image.load("Jirachi1.png")
JirachiPng1 = pygame.transform.scale(JirachiPng1,(250,250))
Jirachi = Pokemon("Jirachi",Type([List_type.Psy,List_type.Acier]),[JirachiPng,JirachiPng1],pv=341,atk=236,defense=236)
Jirachi.getCompetence()

MagnezonePng = pygame.image.load("Magnezone.png")
MagnezoneIcon = MagnezonePng
MagnezonePng = pygame.transform.scale(MagnezonePng,(250,250))
MagnezonePng1 = pygame.image.load("Magnezone1.png")
MagnezonePng1 = pygame.transform.scale(MagnezonePng1,(250,250))
Magnezone = Pokemon("Magnezone",Type([List_type.Electrique,List_type.Acier]),[MagnezonePng,MagnezonePng1],pv=281,atk=296,defense=266)
Magnezone.getCompetence()

HippodocusPng = pygame.image.load("Hippodocus.png")
HippodocusIcon = HippodocusPng
HippodocusPng = pygame.transform.scale(HippodocusPng,(250,250))
HippodocusPng1 = pygame.image.load("Hippodocus1.png")
HippodocusPng1 = pygame.transform.scale(HippodocusPng1,(250,250))
Hippodocus = Pokemon("Hippodocus",Type(List_type.Sol),[HippodocusPng,HippodocusPng1],pv=357,atk=260,defense=272)
Hippodocus.getCompetence()

AirmurePng = pygame.image.load("Airmure.png")
AirmureIcon = AirmurePng
AirmurePng = pygame.transform.scale(AirmurePng,(250,250))
AirmurePng1 = pygame.image.load("Airmure1.png")
AirmurePng1 = pygame.transform.scale(AirmurePng1,(250,250))
Airmure = Pokemon("Airmure",Type([List_type.Acier,List_type.Vol]),[AirmurePng,AirmurePng1],pv=271,atk=196,defense=316)
Airmure.getCompetence()

ChapignonPng = pygame.image.load("Chapignon.png")
ChapignonIcon = ChapignonPng
ChapignonPng = pygame.transform.scale(ChapignonPng,(250,250))
ChapignonPng1 = pygame.image.load("Chapignon1.png")
ChapignonPng1 = pygame.transform.scale(ChapignonPng1,(250,250))
Chapignon = Pokemon("Chapignon",Type([List_type.Plante,List_type.Combat]),[ChapignonPng,ChapignonPng1],pv=261,atk=296,defense=196)
Chapignon.getCompetence()

LatiasPng = pygame.image.load("Latias.png")
LatiasIcon = LatiasPng
LatiasPng = pygame.transform.scale(LatiasPng,(250,250))
LatiasPng1 = pygame.image.load("Latias1.png")
LatiasPng1 = pygame.transform.scale(LatiasPng1,(250,250))
Latias = Pokemon("Latias",Type([List_type.Dragon,List_type.Psy]),[LatiasPng,LatiasPng],pv=301,atk=256,defense=296)
Latias.getCompetence()

StarossPng = pygame.image.load("Staross.png")
StarossIcon = StarossPng
StarossPng = pygame.transform.scale(StarossPng,(250,250))
StarossPng1 = pygame.image.load("Staross1.png")
StarossPng1 = pygame.transform.scale(StarossPng1,(250,250))
Staross = Pokemon("Staross",Type([List_type.Eau,List_type.Psy]),[StarossPng,StarossPng1],pv=261,atk=236,defense=206)
Staross.getCompetence()

AzumarillPng = pygame.image.load("Azumarill.png")
AzumarillIcon = AzumarillPng
AzumarillPng = pygame.transform.scale(AzumarillPng,(250,250))
AzumarillPng1 = pygame.image.load("Azumarill1.png")
AzumarillPng1 = pygame.transform.scale(AzumarillPng1,(250,250))
Azumarill = Pokemon("Azumarill",Type([List_type.Eau,List_type.Psy]),[AzumarillPng,AzumarillPng1],pv=341,atk=156,defense=196)
Azumarill.getCompetence()

TyranocifPng = pygame.image.load("Tyranocif.png")
TyranocifIcon = TyranocifPng
TyranocifPng = pygame.transform.scale(TyranocifPng,(250,250))
TyranocifPng1 = pygame.image.load("Tyranocif1.png")
TyranocifPng1 = pygame.transform.scale(TyranocifPng1,(250,250))
Tyranocif = Pokemon("Tyranocif",Type([List_type.Tenebre,List_type.Roche]),[TyranocifPng,TyranocifPng1],pv=341,atk=304,defense=256)
Tyranocif.getCompetence()

list_poke = [Dimoret,Lucario,Pingoleon,Simiabraz,Mackogneur,Scorvol,Leviator,Cizayox,Elechtor,Leuphorie,Ectoplasma,Jirachi,Magnezone,Hippodocus,Airmure,Chapignon,Latias,Staross,Azumarill,Tyranocif]
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
        for i in range(len(self.pokemon.type.img)):
            screen.blit(self.pokemon.type.img[i],(self.x+140+i*50,self.y+20))
        screen.blit(pokeVie,(self.x+50,self.y+50))
        
    def drawSelect(self):
        if pygame.mouse.get_pressed()[0] and self.x+40 <= pygame.mouse.get_pos()[0] <= self.x+100 and self.y+40 <= pygame.mouse.get_pos()[1] <= self.y+100:
            if Dimoret.etat == "vie":
                Team.append(Dimoret)
                Dimoret.img = Dimoret.img[1]
                Dimoret.etat = "mort"
        elif pygame.mouse.get_pressed()[0] and self.x+240 <= pygame.mouse.get_pos()[0] <= self.x+300 and self.y+40 <= pygame.mouse.get_pos()[1] <= self.y+100:
            if Lucario.etat == "vie":
                Team.append(Lucario)
                Lucario.img = Lucario.img[1]
                Lucario.etat = "mort"
        elif pygame.mouse.get_pressed()[0] and self.x+440 <= pygame.mouse.get_pos()[0] <= self.x+500 and self.y+40 <= pygame.mouse.get_pos()[1] <= self.y+100:
            if Pingoleon.etat == "vie":
                Team.append(Pingoleon)
                Pingoleon.img = Pingoleon.img[1]
                Pingoleon.etat = "mort"
        elif pygame.mouse.get_pressed()[0] and self.x+640 <= pygame.mouse.get_pos()[0] <= self.x+700 and self.y+40 <= pygame.mouse.get_pos()[1] <= self.y+100:
            if Simiabraz.etat == "vie":
                Team.append(Simiabraz)
                Simiabraz.img = Simiabraz.img[1]
                Simiabraz.etat = "mort"
        elif pygame.mouse.get_pressed()[0] and self.x+840 <= pygame.mouse.get_pos()[0] <= self.x+900 and self.y+40 <= pygame.mouse.get_pos()[1] <= self.y+100:
            if Mackogneur.etat == "vie":
                Team.append(Mackogneur)
                Mackogneur.img = Mackogneur.img[1]
                Mackogneur.etat = "mort"
        elif pygame.mouse.get_pressed()[0] and self.x+40 <= pygame.mouse.get_pos()[0] <= self.x+100 and self.y+150 <= pygame.mouse.get_pos()[1] <= self.y+210:
            if Scorvol.etat == "vie":
                Team.append(Scorvol)
                Scorvol.img = Scorvol.img[1]
                Scorvol.etat = "mort"
        elif pygame.mouse.get_pressed()[0] and self.x+240 <= pygame.mouse.get_pos()[0] <= self.x+300 and self.y+150 <= pygame.mouse.get_pos()[1] <= self.y+210:
            if Leviator.etat == "vie":
                Team.append(Leviator)
                Leviator.img = Leviator.img[1]
                Leviator.etat = "mort"
        elif pygame.mouse.get_pressed()[0] and self.x+440 <= pygame.mouse.get_pos()[0] <= self.x+500 and self.y+150 <= pygame.mouse.get_pos()[1] <= self.y+210:
            if Cizayox.etat == "vie":
                Team.append(Cizayox)
                Cizayox.img = Cizayox.img[1]
                Cizayox.etat = "mort"
        elif pygame.mouse.get_pressed()[0] and self.x+640 <= pygame.mouse.get_pos()[0] <= self.x+700 and self.y+150 <= pygame.mouse.get_pos()[1] <= self.y+210:
            if Elechtor.etat == "vie":
                Team.append(Elechtor)
                Elechtor.img = Elechtor.img[1]
                Elechtor.etat = "mort"
        elif pygame.mouse.get_pressed()[0] and self.x+840 <= pygame.mouse.get_pos()[0] <= self.x+900 and self.y+150 <= pygame.mouse.get_pos()[1] <= self.y+210:
            if Leuphorie.etat == "vie":
                Team.append(Leuphorie)
                Leuphorie.img = Leuphorie.img[1]
                Leuphorie.etat = "mort"
        elif pygame.mouse.get_pressed()[0] and self.x+40 <= pygame.mouse.get_pos()[0] <= self.x+100 and self.y+260 <= pygame.mouse.get_pos()[1] <= self.y+320:
            if Ectoplasma.etat == "vie":
                Team.append(Ectoplasma)
                Ectoplasma.img = Ectoplasma.img[1]
                Ectoplasma.etat = "mort"
        elif pygame.mouse.get_pressed()[0] and self.x+240 <= pygame.mouse.get_pos()[0] <= self.x+300 and self.y+260 <= pygame.mouse.get_pos()[1] <= self.y+320:
            if Jirachi.etat == "vie":
                Team.append(Jirachi)
                Jirachi.img = Jirachi.img[1]
                Jirachi.etat = "mort"
        elif pygame.mouse.get_pressed()[0] and self.x+440 <= pygame.mouse.get_pos()[0] <= self.x+500 and self.y+260 <= pygame.mouse.get_pos()[1] <= self.y+320:
            if Magnezone.etat == "vie":
                Team.append(Magnezone)
                Magnezone.img = Magnezone.img[1]
                Magnezone.etat = "mort"
        elif pygame.mouse.get_pressed()[0] and self.x+640 <= pygame.mouse.get_pos()[0] <= self.x+700 and self.y+260 <= pygame.mouse.get_pos()[1] <= self.y+320:
            if Hippodocus.etat == "vie":
                Team.append(Hippodocus)
                Hippodocus.img = Hippodocus.img[1]
                Hippodocus.etat = "mort"
        elif pygame.mouse.get_pressed()[0] and self.x+840 <= pygame.mouse.get_pos()[0] <= self.x+900 and self.y+260 <= pygame.mouse.get_pos()[1] <= self.y+320:
            if Airmure.etat == "vie":
                Team.append(Airmure)
                Airmure.img = Airmure.img[1]
                Airmure.etat = "mort"
        elif pygame.mouse.get_pressed()[0] and self.x+40 <= pygame.mouse.get_pos()[0] <= self.x+100 and self.y+370 <= pygame.mouse.get_pos()[1] <= self.y+430:
            if Chapignon.etat == "vie":
                Team.append(Chapignon)
                Chapignon.img = Chapignon.img[1]
                Chapignon.etat = "mort"
        elif pygame.mouse.get_pressed()[0] and self.x+240 <= pygame.mouse.get_pos()[0] <= self.x+300 and self.y+370 <= pygame.mouse.get_pos()[1] <= self.y+430:
            if Latias.etat == "vie":
                Team.append(Latias)
                Latias.img = Latias.img[1]
                Latias.etat = "mort"
        elif pygame.mouse.get_pressed()[0] and self.x+440 <= pygame.mouse.get_pos()[0] <= self.x+500 and self.y+370 <= pygame.mouse.get_pos()[1] <= self.y+430:
            if Staross.etat == "vie":
                Team.append(Staross)
                Staross.img = Staross.img[1]
                Staross.etat = "mort"
        elif pygame.mouse.get_pressed()[0] and self.x+640 <= pygame.mouse.get_pos()[0] <= self.x+700 and self.y+370 <= pygame.mouse.get_pos()[1] <= self.y+430:
            if Azumarill.etat == "vie":
                Team.append(Azumarill)
                Azumarill.img = Azumarill.img[1]
                Azumarill.etat = "mort"
        elif pygame.mouse.get_pressed()[0] and self.x+840 <= pygame.mouse.get_pos()[0] <= self.x+900 and self.y+370 <= pygame.mouse.get_pos()[1] <= self.y+430:
            if Tyranocif.etat == "vie":
                Team.append(Tyranocif)
                Tyranocif.img = Tyranocif.img[1]
                Tyranocif.etat = "mort"
        screen.blit(self.img,(self.x,self.y))
        if Dimoret.etat == "vie":
            screen.blit(dimoretIcon,(self.x+40,self.y+40))
        if Lucario.etat == "vie":
            screen.blit(LucarioIcon,(self.x+240,self.y+40))
        if Pingoleon.etat == "vie":
            screen.blit(PingoleonIcon,(self.x+440,self.y+40))
        if Simiabraz.etat == "vie":
            screen.blit(SimiabrazIcon,(self.x+640,self.y+40))
        if Mackogneur.etat == "vie":
            screen.blit(MackogneurIcon,(self.x+840,self.y+40))
        if Scorvol.etat == "vie":
            screen.blit(ScorvolIcon,(self.x+40,self.y+150))
        if Leviator.etat == "vie":
            screen.blit(LeviatorIcon,(self.x+240,self.y+150))
        if Cizayox.etat == "vie":
            screen.blit(CizayoxIcon,(self.x+440,self.y+150))
        if Elechtor.etat == "vie":
            screen.blit(ElechtorIcon,(self.x+640,self.y+150))
        if Leuphorie.etat == "vie":
            screen.blit(LeuphorieIcon,(self.x+840,self.y+150))
        if Ectoplasma.etat == "vie":
            screen.blit(EctoplasmaIcon,(self.x+40,self.y+260))
        if Jirachi.etat == "vie":
            screen.blit(JirachiIcon,(self.x+240,self.y+260))
        if Magnezone.etat == "vie":
            screen.blit(MagnezoneIcon,(self.x+440,self.y+260))
        if Hippodocus.etat == "vie":
            screen.blit(HippodocusIcon,(self.x+640,self.y+260))
        if Airmure.etat == "vie":
            screen.blit(AirmureIcon,(self.x+840,self.y+260))
        if Chapignon.etat == "vie":
            screen.blit(ChapignonIcon,(self.x+40,self.y+370))
        if Latias.etat == "vie":
            screen.blit(LatiasIcon,(self.x+240,self.y+370))
        if Staross.etat == "vie":
            screen.blit(StarossIcon,(self.x+440,self.y+370))
        if Azumarill.etat == "vie":
            screen.blit(AzumarillIcon,(self.x+640,self.y+370))
        if Tyranocif.etat == "vie":
            screen.blit(TyranocifIcon,(self.x+840,self.y+370))
        
        
    def drawText(self):

        screen.blit(self.img,(self.x,self.y))
        attaque = []
        for i in range(4):
            if i == self.index:
                attaque.append(capacityFont.render(str(self.pokemon.competence[i].nom) +" | " + str(self.pokemon.competence[i].degat),True,(255,10,10)))
            else:
                attaque.append(capacityFont.render(str(self.pokemon.competence[i].nom) +" | " + str(self.pokemon.competence[i].degat),True,(10,10,10)))
        screen.blit(attaque[0],(self.x+50,self.y+40))
        screen.blit(attaque[1],(self.x+250,self.y+40))
        screen.blit(attaque[2],(self.x+50,self.y+90))
        screen.blit(attaque[3],(self.x+250,self.y+90))
        teamChange = []
        for i in range(6):
            if Team[i].etat == "mort":
                teamChange.append(font.render(str(Team[i].getName()),True,(150,150,150)))
            elif i == Team.index(partie.pokemon1):
                teamChange.append(font.render(str(Team[i].getName()),True,(50,50,150)))
            elif i == self.index-4:
                teamChange.append(font.render(str(Team[i].getName()),True,(255,5,5)))
            else:
                teamChange.append(font.render(str(Team[i].getName()),True,(5,5,5)))
        screen.blit(teamChange[0],(self.x+700,self.y+40))
        screen.blit(teamChange[1],(self.x+700,self.y+75))
        screen.blit(teamChange[2],(self.x+700,self.y+110))
        screen.blit(teamChange[3],(self.x+850,self.y+40))
        screen.blit(teamChange[4],(self.x+850,self.y+75))
        screen.blit(teamChange[5],(self.x+850,self.y+110))
        
    def getIndex(self):
        global run
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_LEFT:
                    self.index -=1
                elif event.key == pygame.K_RIGHT:
                    self.index +=1
                elif event.key == pygame.K_a:
                    if self.index >= 0 and self.index <4:
                        partie.attaque(0,self.index)
                        partie.verifieFin() 
                        if partie.verifieFin() == "Changement":
                            return True
                        elif partie.verifieFin() == "Victoire":
                            run = False
                            return True
                        partie.attaque(1,random.randint(0,3))
                        partie.verifieFin()
                        if partie.verifieFin() == "Defaite":
                                run = False
                                return True
                    else:
                        if Team.index(partie.pokemon1) != self.index-4:
                            partie.pokemon1 = Team[self.index-4]

                            partie.pokemon1.x =160
                            partie.pokemon1.y = 220
                            partie.pokemon1.img = partie.pokemon1.img
                            partie.attaque(1,random.randint(0,3))
                            partie.verifieFin()
                            if partie.verifieFin() == "Defaite":
                                    run = False
                                    return True
            elif self.index > 9:
                self.index -= 9
    
Team = []
TeamEnemy = []

partie = Combat(P2,P1)
partie.pokemon1.x =160
partie.pokemon1.y = 220
partie.pokemon2.x = 550
partie.pokemon2.y = 90


pygame.init()

screen = pygame.display.set_mode((1050,540))
background = pygame.image.load('background_pokemon.jpg')
pygame.display.set_caption("Combat Pokemon")
font = pygame.font.Font('freesansbold.ttf',15)
cadreSelectImg = pygame.image.load("Back-Select.png")
capacityFont = pygame.font.Font('freesansbold.ttf',20)
cadreImg = pygame.image.load("cadreText.png")
cadrePokemonImg = pygame.image.load("cadrePokemon.png")
cadrePokemonImg2 = pygame.image.load("cadrePokemon2.png")
cadreSelect = Cadre(cadreSelectImg,0,0,partie.pokemon1)
cadreText = Cadre(cadreImg,0,390,partie.pokemon1)
cadrePokemon = Cadre(cadrePokemonImg,50,100,partie.pokemon1)
cadrePokemon2 = Cadre(cadrePokemonImg2,700,290,partie.pokemon2)
run = True
choix_menu = 0
while run:
    if choix_menu == 0:
        screen.fill((35,35,205))
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
        cadreSelect.drawSelect()
        cadreSelect.getIndex()
        if len(Team) == 6:
            random.shuffle(list_poke)
            poke = 0
            index = 0
            while poke <= 5:
                if list_poke[index].etat == "vie":
                    list_poke[index].img =  list_poke[index].img[0]
                    list_poke[index].etat == "mort"
                    TeamEnemy.append(list_poke[index])
                    poke+=1
                index +=1
                    
            for i in Team:
                i.etat = "vie"
            for i in TeamEnemy:
                i.etat = "vie"
            partie.pokemon1 = Team[0]
            partie.pokemon1.x =160
            partie.pokemon1.y = 220 
            partie.pokemon2 = TeamEnemy[0]
            partie.pokemon2.x = 550
            partie.pokemon2.y = 90
            choix_menu = 1
    elif choix_menu == 1:
        screen.fill((35,35,35))
        screen.blit(background, (0,0))
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
        
        partie.draw(0)
        partie.draw(1)
        cadreText.pokemon = partie.pokemon1
        cadreText.drawText()
        cadreText.getIndex()
        cadrePokemon.drawPokemon()
        cadrePokemon.pokemon = partie.pokemon1
        cadrePokemon2.drawPokemon()
        cadrePokemon2.pokemon = partie.pokemon2
    
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
        