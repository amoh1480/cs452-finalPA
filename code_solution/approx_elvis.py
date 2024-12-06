################################################
# Deterministic
# assign arbitrary order to the edges

# V = {}

# foreach (edge e in edgeList)

#   if both vertices are not taken

#     take both vertices and remove incident edges

#   else ignore both vertices

# VC = V
################################################
# Probablistic
# assign arbitrary order to the edges

# V = {}

# foreach (edge e in edgeList)

#   take one endpoint at random

#   Remove edges incident to the chosen endpoint

# VC = V

import matplotlib.pyplot as plt
import networkx as nx


# https://www.geeksforgeeks.org/searching-algorithms-for-a-2d-arrays-matrix/
# Didn't really work for removing due to decreasing array size but idea came
# from this site
def removeElement (arr, target):
    i = 0
    while i < len(arr): 
        for j in range(len(arr[i])):
            if arr[i][j] == target:
                print("deleted: ", arr[i])
                del arr[i]
                i -= 1 
                break # Need this 
        i += 1
    return

# http://tandy.cs.illinois.edu/dartmouth-cs-approx.pdf
# Basically this idea - need to test fully.. no clue if it really works
def vertex_cover_prob(graph):
    V = []
    
    for edge in graph: 
        V.append(edge[0])
        V.append(edge[1])
        removeElement(graph, edge[0])
        removeElement(graph, edge[1])
        print(graph)
    
    return V


def visualize_graph(edges):
    G = nx.Graph()
    G.add_edges_from(edges)
    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, font_weight='bold')
    plt.show()


def main():
    # Read the input
    data = []
    # num_edges = input("Number of edges: ")
    while True:
        try:
            # Read a line of input
            line = input().strip()
            if not line:  # Stop if input is empty
                break
            data.append(list(map(str, line.split())))
        except EOFError:  # Stop on EOF
            break
    # print(num_edges)
    print(data)
    
    min_vertex = vertex_cover_prob(data)
    print(min_vertex)
    
    return

if __name__ == '__main__':
    main()