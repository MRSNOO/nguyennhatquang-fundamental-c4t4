stringnhapvao = input("nhap vao:")
letter_counts = {}
for letter in stringnhapvao:
    if letter != " ":
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
items = list(letter_counts.items())
items.sort()
for keys,values in items:
    print(keys," ",values)
