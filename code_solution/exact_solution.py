import itertools
import time


def exact_solution(graph):
    # Go through all the vertices of the graph
    for i in range(1, len(graph.vertices) + 1):
        # Check the subsets of size i 
        for subset in itertools.combinations(graph.vertices, i):
            # Check if the subset is a vertex cover
            if vertification(graph, subset):
                return subset
    # Return none if no vertex cover is found
    return None


def vertification(graph, vertex_cover):
    # go through all edges in the graph 
    for edge in graph.edges: # having your own class is goated #shout out mitre internship
        # Check if in the vertex cover
        if edge[0] not in vertex_cover and edge[1] not in vertex_cover:
            return False
    return True


def main():
    # Start the time of the algorithm
    start_time = time.time()
    # Read in the input from the files
    edges_amount = int(input().strip())
    edges = set([tuple(input().split()) for i in range(edges_amount)])
    # Create graph that contains the edges and vertices
    graph = Graph(edges) 
    # Run the vertex cover algorithm
    vertex_cover = exact_solution(graph)
    # Find the runtime of the algo
    end_time = time.time() 
    runtime = end_time - start_time  

    # print the results
    print(len(vertex_cover))
    print(" ".join(vertex_cover))
    print("Runtime: ", runtime)

# custom graph, where edges are (a, b), ... , (?, ?)
class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.vertices = set()
        for edge in edges:
            self.vertices.update(edge)

if __name__ == "__main__":
    main()