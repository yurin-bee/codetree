from itertools import groupby

A = input()

encodded = ''.join(f"{char}{len(list(lst))}" for char, lst in groupby(A))
print(len(encodded))
print(encodded)