from enum import Enum, auto
from pokemon import Pokemon


class List_type(Enum):
    Feu = auto()
    Eau = auto()
    Plante = auto()
    Electrique = auto()
    Normal = auto()
    Glace = auto()
    Combat = auto()
    Poison = auto()
    Sol = auto()
    Vol = auto()
    Psy = auto()
    Insecte = auto()
    Roche = auto()
    Spectre = auto()
    Dragon = auto()
    Tenebre = auto()
    Acier = auto()
    
#Je crée un dictionnaire, pour chaque type, une liste avec la première liste contenant les attaques super efficace, et la deuxieme les attaque peu efficaces
#De La forme TableDesTypes["type"] = [[Les types super efficace],[Les types peu efficace],[Les type pas efficace]]
TableDesTypes = {
    str(List_type.Feu):[[List_type.Plante,List_type.Glace,List_type.Insecte,List_type.Acier],[List_type.Eau,List_type.Feu,List_type.Roche,List_type.Dragon],[]],
    str(List_type.Eau):[[List_type.Feu,List_type.Sol,List_type.Roche],[List_type.Plante,List_type.Eau,List_type.Dragon],[]],
    str(List_type.Plante):[[List_type.Eau,List_type.Sol,List_type.Roche],[List_type.Feu,List_type.Plante,List_type.Poison,List_type.Vol,List_type.Insecte,List_type.Dragon,List_type.Acier],[]],
    str(List_type.Electrique):[[List_type.Eau,List_type.Vol],[List_type.Plante,List_type.Electrique,List_type.Dragon],[List_type.Sol]],
    str(List_type.Normal):[[],[List_type.Roche,List_type.Acier],[List_type.Spectre]],
    str(List_type.Glace):[[List_type.Plante,List_type.Sol,List_type.Vol,List_type.Dragon],[List_type.Feu,List_type.Eau,List_type.Glace,List_type.Acier],[]],
    str(List_type.Combat):[[List_type.Normal,List_type.Glace,List_type.Roche,List_type.Tenebre,List_type.Acier],[List_type.Poison,List_type.Vol,List_type.Psy,List_type.Insecte],[List_type.Spectre]],
    str(List_type.Poison):[[List_type.Plante],[List_type.Poison,List_type.Sol,List_type.Roche,List_type.Spectre],[List_type.Acier]],
    str(List_type.Sol):[[List_type.Feu,List_type.Electrique,List_type.Poison,List_type.Roche,List_type.Acier],[List_type.Plante,List_type.Insecte],[List_type.Vol]],
    str(List_type.Vol):[[List_type.Plante,List_type.Combat,List_type.Insecte],[List_type.Electrique,List_type.Roche,List_type.Acier],[]],
    str(List_type.Psy):[[List_type.Combat,List_type.Poison],[List_type.Psy,List_type.Acier],[List_type.Tenebre]],
    str(List_type.Insecte):[[List_type.Plante,List_type.Psy,List_type.Tenebre],[List_type.Feu,List_type.Combat,List_type.Poison,List_type.Vol,List_type.Spectre,List_type.Acier],[]],
    str(List_type.Roche):[[List_type.Feu,List_type.Glace,List_type.Vol,List_type.Insecte],[List_type.Combat,List_type.Sol,List_type.Acier],[]],
    str(List_type.Spectre):[[List_type.Psy,List_type.Spectre],[List_type.Tenebre,List_type.Acier],[List_type.Normal]],
    str(List_type.Dragon):[[List_type.Dragon],[List_type.Acier],[]],
    str(List_type.Tenebre):[[List_type.Psy,List_type.Spectre],[List_type.Combat,List_type.Tenebre,List_type.Acier],[]],
    str(List_type.Acier):[[List_type.Glace,List_type.Roche],[List_type.Feu,List_type.Eau,List_type.Acier],[]]
}


class Type():
    
    def __init__(self,type):
        self.type = type
        
    def __repr__(self):
        return f"Type : {self.type}"
    
    def howEffective(self,othertype):
        if type(othertype) != list: 
            for keys in TableDesTypes.keys():
                if keys == str(self.type):
                    if othertype in TableDesTypes[str(self.type)][0]:
                        return 2
                    elif othertype in TableDesTypes[str(self.type)][1]:
                        return 0.5 
                    elif othertype in TableDesTypes[str(self.type)][2]:
                        return 0
            return 1
        else:
            total = 1
            for oneType in othertype:
                for keys in TableDesTypes.keys():
                    if keys == str(self.type):
                        if oneType in TableDesTypes[str(self.type)][0]:
                            total *= 2
                        elif oneType in TableDesTypes[str(self.type)][1]:
                            total *= 0.5 
                        elif oneType in TableDesTypes[str(self.type)][2]:
                            total *= 0
                total *= 1
            return total
    