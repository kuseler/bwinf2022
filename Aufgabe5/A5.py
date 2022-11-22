""" GRAPHENTHEORIE: Einfach einen shortest path algorithmus (Moore oder Dijkstra, etc.) benutzen um die kürzesten Wege zu finden"""

import networkx as nx

def read_lines_into_graph(lines):
    return nx.DiGraph((i.split() for i in lines))
    

def find_route_in_graph(graph, start1, start2):
    routes = []
    for i in graph:
        try:
            routes.append((nx.shortest_path(graph,start1, i), nx.shortest_path(graph,start2, i)))
        except nx.exception.NetworkXNoPath:
            pass
    return routes

def main():
    l =  input("Bitte geben Sie die Datei an: ")
    with open(l) as f:
        gr = read_lines_into_graph(f.readlines()[1:])
    routes = []
    for i in gr:
        routes.append((nx.shortest_path(gr, "1", i), nx.shortest_path(gr, "2", i)))
    print(routes)
    routes = min(routes, key=max)
    if routes:
        print(routes)
    else:
        print("Kein Weg möglich")
        

if __name__ == '__main__':
    main()
