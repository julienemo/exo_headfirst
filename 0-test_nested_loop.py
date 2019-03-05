for i in range(0, 4):
    for j in range(0, 4):
        print(i*j)

for word in ['ok', 'cat', 'lion', 'tiger', 'bobcat']:
    for i in range(2, 7):
        letters = len(word)
        if (letters % i) == 0:
            print(i, word)


full = False
donations = []
full_load = 45

toys = ['robot', 'doll', 'ball', 'slinky']

while not full:
    for toy in toys:
        donations.append(toy)
        size = len(donations)
        if (size >= full_load):
            full = True
print('Full with', len(donations), 'toys')
print(donations)
