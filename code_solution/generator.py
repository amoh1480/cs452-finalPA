import random
import string

# Generator for a large bipartite graph
def generate_large_bipartite_graph(file_name, num_vertices):
    num_edges = num_vertices ** 2 
    vertices = list(string.ascii_lowercase + string.digits)
    if num_vertices > len(vertices):
        raise ValueError(f"Number of vertices cannot exceed {len(vertices)}")

    set_size = num_vertices // 2
    set_A = vertices[:set_size]
    set_B = vertices[set_size:num_vertices]

    with open(file_name, "w") as f:
        f.write(f"{num_edges}\n")
        for _ in range(num_edges):
            u = random.choice(set_A)
            v = random.choice(set_B)
            f.write(f"{u} {v}\n")

# Example usage
generate_large_bipartite_graph("test_cases/large_graph.txt", 33)