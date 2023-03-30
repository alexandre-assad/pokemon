from competence import *
import pygame
class Pokemon:
    
    def __init__(self,nom,type,img,x=0,y=0,pv=100,atk=1,defense=1):
        self.__nom = nom
        self.type = type
        self.__vie = pv
        self.lvl = 100
        self.atk = atk
        self.deff = defense
        self.competence = []
        self.img = img
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"Pokemon : {self.__nom}; PV : {self.__vie}; Attaque : {self.atk}; Defense : {self.deff}; Level : {self.lvl}"
    
    def draw(self):
        pass
        
    def getName(self):
        return f"{self.__nom}"
    def setName(self,new):
        self.__nom = new
    def getVie(self):
        return self.__vie
    def setVie(self,new):
        self.__vie = new
        
    def getCompetence(self):
        self.competence = randomCompetence(self.type.type)