#!/bin/bash

# Test case 1: Simple graph
echo -e "a b\nb c\nc d\nd e" | python3 approx_elvis.py > output1.txt
echo "Expected output: ['a', 'b', 'c', 'd', 'e']"
echo "Actual output: $(cat output1.txt)"
echo

# Test case 2: Graph with a single edge
echo -e "a b" | python3 approx_elvis.py > output2.txt
echo "Expected output: ['a', 'b']"
echo "Actual output: $(cat output2.txt)"
echo

# Test case 3: Graph with multiple edges sharing vertices
echo -e "a b\nb c\na c" | python3 approx_elvis.py > output3.txt
echo "Expected output: ['a', 'b', 'c']"
echo "Actual output: $(cat output3.txt)"
echo

# Test case 4: Disconnected graph
echo -e "a b\nc d" | python3 approx_elvis.py > output4.txt
echo "Expected output: ['a', 'b', 'c', 'd']"
echo "Actual output: $(cat output4.txt)"
echo

# Test case 5: Empty graph
echo -e "" | python3 approx_elvis.py > output5.txt
echo "Expected output: []"
echo "Actual output: $(cat output5.txt)"
echo

# Test case 6: Complex graph
echo -e "a b\nb c\nc d\nd e\ne f\nf g\ng h\nh i\ni j\nj k\nk l\nl m\nm n\nn o\no p\np q\nq r\nr s\ns t\nt u\nu v\nv w\nw x\nx y\ny z\nz a" | python3 approx_elvis.py > output6.txt
echo "Expected output: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']"
echo "Actual output: $(cat output6.txt)"
echo