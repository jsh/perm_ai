import sys
from itertools import permutations
from sympy.combinatorics.permutations import Permutation

def longest_sublist(lst):
    return max(len(x) for x in lst)

def sort_by_cycle_length(lst, reverse=False):
    return sorted(lst, key=len, reverse=reverse)

def cycles(n):
    c = [p.full_cyclic_form for p in (Permutation(_) for _ in permutations(range(n)))]
    return c

def get_argument():
    if len(sys.argv) > 1:
        try:
            return int(sys.argv[1])
        except ValueError:
            pass
    return 3

def main():
    c = cycles(get_argument())
    print(c)

    c = sort_by_cycle_length(c, reverse=True)
    print(c)

if __name__ == "__main__":
    main()