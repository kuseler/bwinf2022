""" GRAPHENTHEORIE: Einfach einen shortest path algorithmus (Moore oder Dijkstra, etc.) benutzen um die kürzesten Wege zu finden"""
# Alternativ: durch die Nachbarsnachbarn iterieren
from graph import *

def create_graph(lines):
    graph = Graph()
    for i in lines:
        graph.addKante(*i.split(" "))
        print(*i.split(" "))
    return graph

with open("huepfburg0.txt") as f:
    a = create_graph(f.readlines()[1:])



def get_near(start, graph):
    own_graph = dict({start:[graph[start]]})
    return own_graph

def find_next_neighbours(start, graph):
    graph[start].append([])
    for i in graph[start][-2]:
        #print("a:",graph[i])
        graph[start][-1] += graph[i][-1]
        
        
def clean_up_associations(graph, start):
    g=graph[start][::-1]
    for i,j in enumerate(g[:-1]):
        j = list(set(j))
        j = list(filter(lambda x : x not in [k for l in g[i+1:] for k in l], j))
        g[i] = j
        print("j: ",g[i])
    return g[::-1]

def main():
    for i in range(3):
        find_next_neighbours("1", a)
    for i in range(3):
        find_next_neighbours("2", a)
    clean_up_associations(a, "1")
    clean_up_associations(a, "2")


def finde_nachbarn(graph, start):
    return graph[start]
