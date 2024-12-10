import itertools
import sys

# https://www.geeksforgeeks.org/finding-minimum-vertex-cover-graph-using-binary-search/
# curious solution 


# Find the minimum vertex cover for a given graph, exact solution 
# generate all the subsets of the vertices and see if they're a vertex cover
# Solution inspired by this
# https://stackoverflow.com/questions/66513948/brute-force-exact-algorithm-for-vertex-cover
def exact_solution(graph):
    # Go through all the vertices of the graph
    for i in range(1, len(graph.vertices) + 1):
        # Using itertools, create all subets of the graph
        # using itetools combinations where the first input is the combinations and second one is 
        # the amount of elements in the combination, based off i. Once it's vertified, you can return right away
        # without checkign for a minimum, as it's the first one found from 0
        for subset in itertools.combinations(graph.vertices, i):
            # Check if the subset is a vertex cover
            if vertification(graph, subset):
                return subset
    # Return none if no vertex cover is found
    return None


def vertification(graph, vertex_cover):
    # go through all edges in the graph 
    for edge in graph.edges: # having your own class is goated #shout out mitre internship
        # Check if in vertex cover or not 
        # Edge is in the shape of (a, b) where a and b are vertices connected by the edge
        if edge[0] not in vertex_cover and edge[1] not in vertex_cover:
            return False
    return True


def main():
    # read in files 
    edges_amount = int(input().strip())
    edges = set([tuple(input().split()) for i in range(edges_amount)])
    graph = Graph(edges) 
    vertex_cover = exact_solution(graph)
    
    print(len(vertex_cover))
    print(" ".join(vertex_cover))

# custom graph, where edges are (a, b), ... , (?, ?)
class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.vertices = set()
        for edge in edges:
            self.vertices.update(edge)

if __name__ == "__main__":
    main()