"""
    Approximate algorithm by Ozi Valdez.
    This is a greedy algorithm that chooses the vertex with the highest edge degree, adds it to the vertex cover, removes its edges, repeats.
    Ummmmmm is this too similar to Elvis'? IDK! lol hehe
    also IDK the runtime yet! whoops!
    got the idea from here: https://people.cs.georgetown.edu/jthaler/ANLY550/lec20.pdf
    bc all the other algorithm ideas i saw were like way too smart like linear programming and stuff like omg nah
"""
def vertex_cover(vertices, edges):
    output = set()
    
    graph = {v: set() for v in vertices}
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    while edges:
        best = max(graph, key = lambda vertex: len(graph[vertex])) # python lambda functions are weird
        print(f"{best} with length {len(graph[best])}")

        output.add(best)

        neighbors = graph[best]

        for neighbor in neighbors:
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

    print(vertex_cover(vertices, edges))

if __name__ == "__main__":
    # # https://commons.wikimedia.org/wiki/File:Vertex-cover.svg#/media/File:Vertex-cover.svg
    # # this photo from wikipedia

    # # first example from that wikipedia link
    # vertices = {'a', 'b', 'c', 'd', 'e', 'f'}
    # edges = {('a', 'b'), ('a', 'c'), ('c', 'f'), ('c', 'e'), ('c', 'd'), ('c', 'b')}
    # print(vertex_cover(vertices, edges)) # should be C, B or C, A (2), which is da best

    # # second example from the wikipedia link
    # vertices = {'a', 'b', 'c', 'd', 'e', 'f'}
    # edges = {('a', 'b'), ('a', 'c'), ('c', 'b'), ('c', 'e'), ('e', 'd'), ('d', 'f')}
    # print(vertex_cover(vertices, edges)) # should be B, C, D or some combination (3), which is da best

    # example from slides
    vertices = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'}
    edges = {('a', 'b'), ('a', 'c'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('d', 'f'), ('d', 'i'), ('i', 'f'), ('i', 'g'), ('i', 'h'), ('f', 'g'), ('g', 'h')}
    print(vertex_cover(vertices, edges)) # should be B, C, D, I, G or some combination (5), which is da best

    # # example that breaks it from the article i stole this from
    # vertices = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'}
    # edges = {('a', 'b'), ('a', 'c'), ('a', 'd'), ('a', 'e'), ('b', 'h'), ('b', 'f'), ('c', 'i'), ('c', 'f'), ('d', 'j'), ('d', 'g'), ('e', 'k'), ('e', 'g')}
    # print(vertex_cover(vertices, edges)) # will give us 7 vertices when it should be 4

    # # also breaks with a triangle
    # vertices = {'a', 'b', 'c'}
    # edges = {('a', 'b'), ('b', 'c'), ('a', 'c')}
    # print(vertex_cover(vertices, edges)) # gives us 2 when it should be 1
    
    # main()