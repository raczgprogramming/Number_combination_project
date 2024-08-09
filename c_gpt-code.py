from collections import Counter
from itertools import combinations

# Minta mátrix
matrix = [
    [3, 7, 9, 11, 32, 54, 45, 49, 48, 33],
    [3, 7, 9, 11, 32, 45, 54, 49, 48, 33],
    [1, 3, 5, 7, 11, 13, 17, 19, 33, 35],
    # További sorok...
]


# Az összes sor kombinációinak számolása
all_combinations = [tuple(row) for row in matrix]

# Számoljuk meg a kombinációk gyakoriságát
combination_counts = Counter(all_combinations)

# A leggyakoribb kombináció kiválasztása
most_common_combination = combination_counts.most_common(1)

print("A leggyakoribb kombináció:", most_common_combination)

# Az összes sor 5-ös kombinációinak számolása
all_five_combinations = []
for row in matrix:
    row_combinations = combinations(row, 5)
    all_five_combinations.extend(row_combinations)

# Számoljuk meg a kombinációk gyakoriságát
combination_five_counts = Counter(all_five_combinations)

# A leggyakoribb kombináció kiválasztása
most_common_five_combination = combination_five_counts.most_common(1)

print("A leggyakoribb 5 elemű kombináció:", most_common_five_combination)