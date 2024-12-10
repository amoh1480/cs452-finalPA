#!/bin/bash


python3 approx_elvis.py > output_files/elvis-result.txt

./ozi_test_cases.sh

./exact_test_cases.sh