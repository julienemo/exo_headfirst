# reading a file as a whole
my_file = open('lib.txt', 'r')
template = my_file.read()
print(template)
my_file.close()

# reading line by line
my_file = open('lib.txt', 'r')
while True:
    line = my_file.readline()
    if line != '':
        print(line)
    else:
        break
my_file.close()

# reading line by line autrement
my_file = open('lib.txt', 'r')
for line in my_file:
    print(line)
my_file.close()

# when testing, noted that need to open and close for each method
# meaning .readline() really know where the last lecture Stop
# any lecture, not just .readline() lectures
# file.read() knows as well

my_file = open('lib.txt', 'r')
lines = []
for index, line in enumerate(my_file):
    lines.append(index)
print(lines[-1])
my_file.close

# une méthode bricolée pour compter le nb de lignes
# il paraît que ça marche pour tout
