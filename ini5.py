# TODO: brief script for only printing the even number lines
import itertools
import sys

with open('rosalind_ini5.txt') as f:
    sys.stdout.writelines(itertools.islice(f, 1, None, 2))