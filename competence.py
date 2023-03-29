from type import *
import random
class Competence:
    
    def __init__(self,nom,type,degat):
        self.nom = nom
        self.type = type
        self.degat = degat
        
    def __repr__(self):
        return f"Attaque : {self.nom} , Type : {self.type} , Degat : {self.degat}\n"
    
#Une liste de 6 compétences par type
listCompetence = {
    str(List_type.Feu): [Competence("Flameche",List_type.Feu,"50"),Competence("Boutefeu",List_type.Feu,"100"),Competence("Flame Croix",List_type.Feu,"75"),Competence("Feu Follet",List_type.Feu,"20"),Competence("Eruption",List_type.Feu,"60"),Competence("Vortex Magma",List_type.Feu,"120")],
    str(List_type.Eau): [Competence("Aqua-Jet",List_type.Eau,"50"),Competence("Octazooka",List_type.Eau,"100"),Competence("HydroVapeur",List_type.Eau,"75"),Competence("Pistolet à O",List_type.Eau,"20"),Competence("Surf",List_type.Eau,"60"),Competence("Hydrocanon",List_type.Eau,"120")],
    str(List_type.Plante): [Competence("Tranche Herbe",List_type.Plante,"50"),Competence("Mega Fouet",List_type.Plante,"100"),Competence("Noeud Herbe",List_type.Plante,"75"),Competence("Balle Graine",List_type.Plante,"20"),Competence("Vege Attaque",List_type.Plante,"60"),Competence("Lance Soleil",List_type.Plante,"120")],
    str(List_type.Electrique): [Competence("Boule Elek",List_type.Electrique,"50"),Competence("Tonnerre",List_type.Electrique,"100"),Competence("Eclair",List_type.Electrique,"75"),Competence("Coup d'jus",List_type.Electrique,"20"),Competence("Electacle",List_type.Electrique,"60"),Competence("Turbo Volt",List_type.Electrique,"120")],
    str(List_type.Normal): [Competence("Charge",List_type.Normal,"50"),Competence("Guillotine",List_type.Normal,"100"),Competence("Plaquage",List_type.Normal,"75"),Competence("Coupe",List_type.Normal,"20"),Competence("Griffe",List_type.Normal,"60"),Competence("Ultralaser",List_type.Normal,"120")],
    str(List_type.Glace): [Competence("Ball'Glace",List_type.Glace,"50"),Competence("Blizzard",List_type.Glace,"100"),Competence("Stalactite",List_type.Glace,"75"),Competence("Grele",List_type.Glace,"20"),Competence("Poing Glace",List_type.Glace,"60"),Competence("Laser Glace",List_type.Glace,"120")],
    str(List_type.Combat): [Competence("Close Combat",List_type.Combat,"50"),Competence("Aurasphere",List_type.Combat,"100"),Competence("Mitra-poing",List_type.Combat,"75"),Competence("Cogne",List_type.Combat,"20"),Competence("Triple Pied",List_type.Combat,"60"),Competence("Surpuissance",List_type.Combat,"120")],
    str(List_type.Poison): [Competence("Acie",List_type.Poison,"50"),Competence("Puredpois",List_type.Poison,"100"),Competence("Cradovague",List_type.Poison,"75"),Competence("Direct Toxik",List_type.Plante,"20"),Competence("Bombe Acide",List_type.Plante,"60"),Competence("Detritus",List_type.Plante,"120")],
    str(List_type.Vol): [Competence("Picpic",List_type.Vol,"50"),Competence("Vol",List_type.Vol,"100"),Competence("Rapace",List_type.Vol,"75"),Competence("Picore",List_type.Vol,"20"),Competence("Lame d'air",List_type.Vol,"60"),Competence("Tornade",List_type.Vol,"120")],
    str(List_type.Sol): [Competence("Osmerang",List_type.Sol,"50"),Competence("Tunnel",List_type.Sol,"100"),Competence("Telluriforce",List_type.Sol,"75"),Competence("Charge Os",List_type.Sol,"20"),Competence("Boue-Bombe",List_type.Sol,"60"),Competence("Seisme",List_type.Sol,"120")],
    str(List_type.Psy): [Competence("Choc Mental",List_type.Psy,"50"),Competence("Rafale Psy",List_type.Psy,"100"),Competence("Devoreve",List_type.Psy,"75"),Competence("Ball'Brume",List_type.Psy,"20"),Competence("Vague Psy",List_type.Psy,"60"),Competence("Lumi-Eclat",List_type.Psy,"120")],
    str(List_type.Insecte): [Competence("Piqure",List_type.Insecte,"50"),Competence("Plaie Croix",List_type.Insecte,"100"),Competence("Survinsect",List_type.Insecte,"75"),Competence("Boule Pollen",List_type.Insecte,"20"),Competence("Megacorne",List_type.Insecte,"60"),Competence("Rayon Signal",List_type.Insecte,"120")],
    str(List_type.Roche): [Competence("Boule Roc",List_type.Roche,"50"),Competence("Eboulement",List_type.Roche,"100"),Competence("Jet Pierres",List_type.Roche,"75"),Competence("Roulage",List_type.Roche,"20"),Competence("Tomberoche",List_type.Roche,"60"),Competence("Pouvoir Antique",List_type.Roche,"120")],
    str(List_type.Spectre): [Competence("Griffe Ombre",List_type.Spectre,"50"),Competence("Rayon Spectral",List_type.Spectre,"100"),Competence("Ball Ombre",List_type.Spectre,"75"),Competence("Lechouilles",List_type.Spectre,"20"),Competence("Ombre Portee",List_type.Spectre,"60"),Competence("Cortege Funebre",List_type.Spectre,"120")],
    str(List_type.Dragon): [Competence("Colere",List_type.Dragon,"50"),Competence("Draco-Choc",List_type.Dragon,"100"),Competence("Draco-souffle",List_type.Dragon,"75"),Competence("Double Baffe",List_type.Dragon,"20"),Competence("Ouragan",List_type.Dragon,"60"),Competence("Laser Infinimax",List_type.Dragon,"120")],
    str(List_type.Tenebre): [Competence("Baston",List_type.Tenebre,"50"),Competence("Explonuit",List_type.Tenebre,"100"),Competence("Punition",List_type.Tenebre,"75"),Competence("Coup bas",List_type.Tenebre,"20"),Competence("Morsure",List_type.Tenebre,"60"),Competence("Vibrobscur",List_type.Tenebre,"120")],
    str(List_type.Acier): [Competence("Queue de Fer",List_type.Acier,"50"),Competence("Lumicanon",List_type.Acier,"100"),Competence("Marteau Mastoc",List_type.Acier,"75"),Competence("Derapage",List_type.Acier,"20"),Competence("Tete de Fer",List_type.Acier,"60"),Competence("Metalaser",List_type.Acier,"120")]
}

def randomCompetence(types):
    listecomp = []
    randomcomp = []
    if type(types) != list:
        listecomp = listCompetence[str(types)]
        random.shuffle(listecomp)
        for i in range (4):
            randomcomp.append(listecomp[i])
    else:
        listecomp1 = listCompetence[str(types[0])]
        listecomp2 = listCompetence[str(types[1])]
        listecomp = listecomp1 + listecomp2
        random.shuffle(listecomp)
        for i in range (4):
            randomcomp.append(listecomp[i])
    return randomcomp