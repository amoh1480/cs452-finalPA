# Simple triangle test
echo "Simple Triangle Test"
echo "Expected: {a}, {b}, or {c} of size 1"
python3 approx_ozi.py <test_cases/simple-triangle.txt >output_files/ozi_simple_triangle.txt
echo "Actual output:"
echo "$(cat output_files/ozi_simple_triangle.txt)"
echo

# Wiki Example 1 test
echo "Wiki Example 1 Test"
echo "Expected: {c, b} or {c, a} of size 2"
python3 approx_ozi.py <test_cases/wiki-example1.txt >output_files/ozi_wiki-example1.txt
echo "Actual output:"
echo "$(cat output_files/ozi_wiki-example1.txt)"
echo

# Wiki Example 2 test
echo "Wiki Example 2 Test"
echo "Expected: {b, c, d} or some combination of size 3"
python3 approx_ozi.py <test_cases/wiki-example2.txt >output_files/ozi_wiki-example2.txt
echo "Actual output:"
echo "$(cat output_files/ozi_wiki-example2.txt)"
echo

# Slides example
echo "Slides example"
echo "Expected: {b, c, d, i, g} or some combination of size 5"
python3 approx_ozi.py <test_cases/slide-example.txt >output_files/ozi_slide-example.txt
echo "Actual output:"
echo "$(cat output_files/ozi_slide-example.txt)"
echo

# Specific case that breaks this example
echo "Breaks Greedy Edge Degree Algorithm"
echo "Expected: {b, c, d, e} or some combination of size 4"
python3 approx_ozi.py <test_cases/greed-article.txt >output_files/ozi_greed-article.txt
echo "Actual output:"
echo "$(cat output_files/ozi_greed-article.txt)"
echo

# Chain graph
echo "Chain Graph"
echo "Expected: {b, c, d} or {a, c, e} or some combination of size 3"
python3 approx_ozi.py <test_cases/chain-graph.txt >output_files/ozi_chain-graph.txt
echo "Actual output:"
echo "$(cat output_files/ozi_chain-graph.txt)"
echo

# Bipartite graph
echo "Bipartite Graph"
echo "Expected: {a, b, c} or {d, e, f} or some combination of size 3"
python3 approx_ozi.py <test_cases/bipartite-graph.txt >output_files/ozi_bipartite-graph.txt
echo "Actual output:"
echo "$(cat output_files/ozi_bipartite-graph.txt)"
echo

# Complete graph
echo "Complete Graph"
echo "Expected: {a, b, c, d, e} or some combination of size 5"
python3 approx_ozi.py <test_cases/complete-graph.txt >output_files/ozi_complete-graph.txt
echo "Actual output:"
echo "$(cat output_files/ozi_complete-graph.txt)"
echo

# Large graph
echo "Extremely Large Graph"
echo "Expected: {???} or some combination of size ????"
python3 approx_ozi.py <test_cases/large_graph.txt >output_files/ozi_large_graph.txt
echo "Actual output:"
echo "$(cat output_files/ozi_large_graph.txt)"
echo