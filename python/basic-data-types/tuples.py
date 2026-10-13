# ==============================================================================
# Solution for Python 3
# Note: In Python 3, hash() uses a random seed per execution, which may cause
# output mismatches on HackerRank test cases.
# ==============================================================================

n = int(input())
print(abs(hash(tuple(map(int, input().split())))))

# ==============================================================================
# Equivalent Solution for Python 2 (Passes HackerRank Test Cases):
#
# n = int(raw_input())
# numbers = tuple(map(int, raw_input().split()))
# print hash(numbers)
# ==============================================================================
