def sum(a, b):
    sum = a + b
    print(sum)
    return sum


sum(3, 4)
another_sum = sum(2, 6)
print(another_sum + 3)
print(sum(7, 5))

# within a func, whenever the prog sees a 'return'
# it returns and stops
# whatever is after is cruely ignored
# so need to put print before return

# whenever a print and return func is called
# (whether to be assigned to a variable or to print)
# the print part will print a visible result
# only if this kind of func is explictly printed
# it'll print twice........
