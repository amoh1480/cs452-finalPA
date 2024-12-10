import time
import os

# https://www.geeksforgeeks.org/searching-algorithms-for-a-2d-arrays-matrix/
# Didn't really work for removing due to decreasing array size but idea came
# from this site
def removeElement (arr, target):
    i = 0
    while i < len(arr): 
        for j in range(len(arr[i])):
            if arr[i][j] == target:
                # print("deleted: ", arr[i])
                del arr[i]
                i -= 1 
                break # Need this 
        i += 1
    return

# http://tandy.cs.illinois.edu/dartmouth-cs-approx.pdf
# Basically this idea - need to test fully.. no clue if it really works
def vertex_cover_prob(graph):
    V = []
    
    start = time.time()
    for edge in graph: 
        edge0 = edge[0]
        edge1 = edge[1]
        V.append(edge0)
        V.append(edge1)
        removeElement(graph, edge0)
        removeElement(graph, edge1)
    end = time.time()
        
    # https://www.geeksforgeeks.org/how-to-check-the-execution-time-of-python-script/
    print(f"\nTime taken: {(end-start)*10**3:.03f}ms")
    return V


def main():
    # Directory containing the test case files
    test_cases_dir = 'test_cases'
    
    # Loop through each file in the test_cases directory
    for filename in os.listdir(test_cases_dir):
        if filename.endswith('.txt'):
            file_path = os.path.join(test_cases_dir, filename)
            data = []
            with open(file_path, 'r') as file:
                lines = file.readlines()
                for line in lines[1:]:
                    line = line.strip()
                    if line:
                        data.append(list(map(str, line.split())))
            # print(f"Input from {filename}: ", data)
            
            min_vertex = vertex_cover_prob(data)
            print(f"Output for {filename}: ", min_vertex)
    
    return

if __name__ == '__main__':
    main()