# CS452 Final PA
- Presentations 
    - A link to the google slide show that describes the problem in depth, 
      with related graph analysis and big-O analysis. 
- Code solution 
    - Output Files 
        - The location of where the files will be outputted once the script is run, showing the subsets that create the vertex cover
    - test_cases
        - A list of the test cases that were used, including a very large test case. Graph types are based off the name of the graph 
    Files:
    - approx_elvis.py 
        - An approximation for the vertex cover problem, choosing an arbritiary edge and adding both vertices to the cover set, and then removing that edge, then repeating. 
    - approx_ozi.py
        - Choose the vertex with the highest degree, remove edges, and then keep going 
    - exact_solution.py
        - go through every vertex, and check every subset of the vertices to see which is the minmum subset
    - generator.py 
        - Generates a graph based off the amount of user inputted vertices. 
    - .sh files
        - Bash files used for running the scripts
# RUNNING 
- To run these scripts, simply do "sh BASHCRIPTNAME.sh" in the command line based off which script you would want to run. Then, go to the output_files folder to see the output of the script, matching the name of the algorithm run.  
