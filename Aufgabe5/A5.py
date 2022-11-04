""" GRAPHENTHEORIE: Einfach einen shortest path algorithmus (Moore oder Dijkstra, etc.) benutzen um die kürzesten Wege zu finden"""
# Alternativ: durch die Nachbarsnachbarn iterieren
#from graph import *

class Graph:
    # Adjazenzliste, nur als Dictionary um Abfragen einfacher und Code lesbarer zu machen
    def __init__(self, graph):
        self.Graph = graph
        
    def add_node(self, start_node, end_node):
        if start_node not in self.Graph:
            self.Graph[start_node] = []
        self.Graph[start_node].append(end_node.strip())
        
    def neighbours(self, start_node):
        try:
            return self.Graph[start_node]
        except KeyError:
            return []

def find(node_list, searched):
    """
    Sucht in einer Liste der Knoten nach dem Element mit bekanntem Knotennamen und unbekannter Entfernung. 
    """
    return list(filter(lambda i: i[0] == searched, lst))[0] 
    

def moore(graph, start):
    g = [(i,"u") for i in set([*[nb for nb_lst in graph.Graph.values() for nb in nb_lst], *graph.Graph.keys()])] 
    #print(f"{g=}")
    g[g.index((start,"u"))] = (start,0)
    to_be_processed = [(start,0)]
    while to_be_processed:
        chosen_node = to_be_processed[0]
        to_be_processed.pop(0)
        for neighbour in graph.neighbours(chosen_node[0]):
            t = find(g, neighbour)[0]
            if t[1]=="u":
                new_distance = chosen_node[1] + 1
                t = (t[0],new_distance)
                g[g.index(find(g, t[0])[0])] = t
                to_be_processed.append(t)
    # since not all nodes are connected to the starting one, we can filter them out:
    
    return list(filter(lambda i: i[1]!="u", g))
                
                
        
def create_graph(lines):
    graph = Graph(dict())
    for i in lines:
        graph.add_node(*i.split(" "))
    return graph


        


def main():
    s=(None,None, 1000)
    with open("huepfburg2.txt") as f:
        a = create_graph(f.readlines()[1:])
    nb1 = moore(a,"1")
    nb2 = moore(a,"2")
    return min(((x,y) for x in nb1 for y in filter(lambda i: i==x,nb2)))

if __name__ == "__main__":
    print(main())
