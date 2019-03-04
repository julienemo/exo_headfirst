def bubble_sort(targets):
    length = len(targets)
    inter = 0
    next_pass = True
    while next_pass is True:
        next_pass = False
        for i in range(length - 1):
            if targets[i] > targets[i + 1]:
                inter = targets[i]
                targets[i] = targets[i + 1]
                targets[i + 1] = inter
                next_pass = True

    print(targets)


list = [9, 8, 7, 5, 3, 1]
menudujour = ['asjd;f', 'iu', 'urtr', 'rtyr', 'rty']

bubble_sort(list)
bubble_sort(menudujour)
