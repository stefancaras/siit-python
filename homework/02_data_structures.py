# ○ declară o listă care conține elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (în această ordine).
# ○ afișează lista inițială ordonată ascendent (lista inițială trebuie păstrată în aceeași formă)
# ○ afișează lista inițială ordonată descendent (lista inițială trebuie păstrată în aceeași formă)
# ○ afișează o listă ce conține numerele pare din lista ordonată (folosind slice)
# ○ afișează o listă ce conține numerele impare din lista ordonată (folosind slice)
# ○ afisează o listă ce conține numerele ce sunt multipli ai numărului 3 (folosind slice)

my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
sorted_list = my_list.copy()
sorted_list.sort()
print(f"Sorted list: {sorted_list}")
print(f"Reversed list: {sorted_list[::-1]}")
print(f"Even numbers: {sorted_list[1::2]}")
print(f"Odd numbers: {sorted_list[::2]}")
print(f"Multiples of 3: {sorted_list[2::3]}")
