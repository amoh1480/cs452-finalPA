import time

"""
    Approximate algorithm by Ozi Valdez.
    This is a greedy algorithm that chooses the vertex with the highest edge degree, adds it to the vertex cover, removes its edges, repeats.
    Got the idea from here: https://people.cs.georgetown.edu/jthaler/ANLY550/lec20.pdf
    Runs in O(V + E)
"""
def vertex_cover(vertices, edges):
    output = set()
    
    graph = {v: set() for v in vertices}
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    while edges: # O(E)
        best = max(graph, key = lambda vertex: len(graph[vertex])) # python lambda functions are weird; also, runs in O(V)

        output.add(best)

        neighbors = graph[best]

        for neighbor in neighbors: # O(E)
            if (best, neighbor) in edges:
                edges.remove((best, neighbor))
            if (neighbor, best) in edges:
                edges.remove((neighbor, best))
            graph[neighbor].remove(best) # forgot to remove it from the graph

        del graph[best]
    
    return output

def main():
    # Read the input
    edges_amount = int(input().strip())
    edges = set([tuple(input().split()) for i in range(edges_amount)])

    vertices = set()
    for edge in edges:
        vertices.add(edge[0])
        vertices.add(edge[1])

    # a = time.time()
    cover = vertex_cover(vertices, edges)
    # b = time.time()
    # print(b - a)

    print(len(cover))
    print(" ".join(cover))

if __name__ == "__main__":
    main()