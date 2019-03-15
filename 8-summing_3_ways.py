# PART I summing items from a list
# task : get the sum of items in the list
list = [10, 13, 39, 14, 41, 9, 3]

# option 1 : built-in sum func
sum(list)


def get_total(target):
    # option 2 : interate
    total = 0
    for n in target:
        total = total + n
    print(total)


def recursive_get_total(target):
    # option 3 : recursive func (calling the func inside itself)
    if len(target) == 0:
        return 0  # it needs to be return instead of print
    else:
        first = target[0]
        rest = target[1:]
        total = first + recursive_get_total(rest)
        return total
