import random
import string

# Chat gpt generator for a large graph
def generate_large_graph(file_name, num_edges):
    vertices = list(string.ascii_letters + string.digits)
    with open(file_name, "w") as f:
        f.write(f"{num_edges}\n")
        for _ in range(num_edges):
            u = random.choice(vertices)
            v = random.choice(vertices)
            while u == v:
                v = random.choice(vertices)
            f.write(f"{u} {v}\n")

generate_large_graph("test_cases/large_graph.txt", 1000000000)