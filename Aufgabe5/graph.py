# Autor: kb
# Datum: 15.07.10

from xml.dom.minidom import *

class Knoten(object):
    def __init__(self, nameKnoten):
        self.name = nameKnoten
        self.kantenZuNachbarn = []
        self.daten = []

    def addNachbar(self, refKante):
        self.kantenZuNachbarn = self.kantenZuNachbarn + [(refKante)]

    def delNachbar(self, refKante):
        neueListe = []
        for kante in self.kantenZuNachbarn:
            if kante != refKante:
                neueListe = neueListe + [kante]
        self.kantenZuNachbarn = neueListe

class Kante(object):
    def __init__(self, refStartKnoten, refZielKnoten):
        self.startKnoten = refStartKnoten
        self.zielKnoten = refZielKnoten
        self.daten = []

class Graph(object):
    def __init__(self):
        self.knotenListe = []

    def getRefKnoten(self, nameKnoten):
        refKnoten = None
        for knoten in self.knotenListe:
            if knoten.name == nameKnoten:
                refKnoten = knoten
        return refKnoten
   
    def addKnoten(self, nameKnoten):
        refKnoten = self.getRefKnoten(nameKnoten)
        if refKnoten == None:
            knoten = Knoten(nameKnoten)
            self.knotenListe = self.knotenListe + [knoten]

    def delKnoten(self, nameKnoten):
        neueListe = []
        for knoten in self.knotenListe:
            if knoten.name != nameKnoten:
                neueListe = neueListe + [knoten]
                neueNachbarn = []
                for kante in knoten.kantenZuNachbarn:
                    if kante.zielKnoten.name != nameKnoten:
                        neueNachbarn = neueNachbarn + [kante]
                knoten.kantenZuNachbarn = neueNachbarn
        self.knotenListe = neueListe    

    def addKante(self, nameStartKnoten, nameZielKnoten):
        self.addKnoten(nameStartKnoten)
        self.addKnoten(nameZielKnoten)
        if self.existiertKnoten(nameStartKnoten) and \
           self.existiertKnoten(nameZielKnoten) and \
           not self.existiertKante(nameStartKnoten, nameZielKnoten):
            refStartKnoten = self.getRefKnoten(nameStartKnoten)
            refZielKnoten = self.getRefKnoten(nameZielKnoten)
            if refStartKnoten != None and refZielKnoten != None:     
                neueKante = Kante(refStartKnoten, refZielKnoten)
                refStartKnoten.addNachbar(neueKante)

    def delKante(self, nameStartKnoten, nameZielKnoten):
        for knoten in self.knotenListe:
            if knoten.name == nameStartKnoten:
                for kante in knoten.kantenZuNachbarn:
                    if kante.zielKnoten.name == nameZielKnoten:
                        knoten.delNachbar(kante)

    def getAlleKnoten(self):
        namenKnoten = []
        for knoten in self.knotenListe:
            namenKnoten = namenKnoten + [knoten.name]
        return namenKnoten

    def getAlleNachbarn(self, nameKnoten):
        refKnoten = self.getRefKnoten(nameKnoten)
        if refKnoten != None:
            listeNachbarn = []
            for kante in refKnoten.kantenZuNachbarn:
                listeNachbarn = listeNachbarn + [kante.zielKnoten.name]
            return listeNachbarn
        else:
            return []

    def existiertKnoten(self, nameKnoten):
        if self.getRefKnoten(nameKnoten) == None:
            return False
        else:
            return True

    def existiertKante(self, nameStartKnoten, nameZielKnoten):
        gefunden = False
        refStartKnoten = self.getRefKnoten(nameStartKnoten)
        refZielKnoten = self.getRefKnoten(nameZielKnoten)
        if refStartKnoten != None and refZielKnoten != None:
            for kante in refStartKnoten.kantenZuNachbarn:
                if kante.zielKnoten == refZielKnoten:
                    gefunden = True
        return gefunden

#----------------------------------------------------------------------

class GraphMitDaten(Graph):
    def __init__(self):
        Graph.__init__(self)

    def addKnotenDaten(self, nameKnoten, datenpaar):
        refKnoten = self.getRefKnoten(nameKnoten)
        if refKnoten != None:
            refKnoten.daten = refKnoten.daten + [datenpaar]

    def addKantenDaten(self, nameStartKnoten, nameZielKnoten, datenpaar):
        refStartKnoten = self.getRefKnoten(nameStartKnoten)
        refZielKnoten = self.getRefKnoten(nameZielKnoten)
        if refStartKnoten != None and refZielKnoten != None:
            for kante in refStartKnoten.kantenZuNachbarn:
                if kante.zielKnoten == refZielKnoten:
                    kante.daten = kante.daten + [datenpaar]

    def getKnotenDaten(self, nameKnoten, key):
        data = None
        refKnoten = self.getRefKnoten(nameKnoten)
        if refKnoten != None:
            data = None
            for d in refKnoten.daten:
                if d[0] == key:
                    data = d[1]
        return data

    def getKantenDaten(self, nameStartKnoten, nameZielKnoten, key):
        data = None
        refStartKnoten = self.getRefKnoten(nameStartKnoten)
        refZielKnoten = self.getRefKnoten(nameZielKnoten)
        if refStartKnoten != None and refZielKnoten != None:
            for kante in refStartKnoten.kantenZuNachbarn:
                if kante.zielKnoten == refZielKnoten:
                    for d in kante.daten:
                        if d[0] == key:
                            data = d[1]
        return data

    def getKantenRefDaten(self, refKante, key):
        data = None
        if refKante != None:
            for d in refKante.daten:
                if d[0] == key:
                    data = d[1]
        return data

