# SEE WHETHER POSSIBLE POUR IMPORT THE LISTS

# there are several bubble solutions to evaluate
# lists of their "scores" and cost are BELOW
scores = [60, 50, 60, 58, 54, 54,
    58, 50, 52, 54,48, 69,
    34, 55, 51, 52, 44, 51,
    69, 64, 66, 55, 52, 61,
    46, 31, 57, 52, 44, 18,
    41, 53, 55, 61, 51, 44]

costs = [.25, .27, .25, .25, .25, .25,
    .33, .31, .25, .29, .27, .22,
    .31, .25, .25, .33, .21, .25,
    .25, .25, .28, .25, .24, .22,
    .20, .25, .30, .25, .24, .25,
    .25, .25, .27, .25, .26, .29]


# 1.print_data :
#   print the phrase "Bubble solution n X, score N" for each solutions
def print_data():  # print the list
    global length
    for i in range(length):
        number_sign = "#"+str(i)
        print('Bubble solution', number_sign, 'score: ', scores[i])


# 2.print_report :
#   the number of solutions tested,
#   highest score,
#   index of highest-scored solution(s)
#   index of solution(s) with highest cost_effectiveness
#   highest N scores and their Index
#   n is chosen by user input
def print_rapport():
    global palmares
    next_pass = True
    positions = list(range(length))
    positions2 = list(range(length))
    cost_effectiveness = []
    for i in range(length):
        cost_effectiveness.append(scores[i] / costs[i])

    while next_pass is True:
        next_pass = False
        for i in range(length-1):
            if scores[i] < scores[i+1]:
                inter = scores[i+1]
                scores[i+1] = scores[i]
                scores[i] = inter
                inter = positions[i+1]
                positions[i+1] = positions[i]
                positions[i] = inter
                next_pass = True

    high_score_solutions = []
    for i in range(length):
        if scores[i] == scores[0]:
            high_score_solutions.append(positions[i])

    next_pass = True
    inter = 0
    while next_pass is True:
        next_pass = False
        for i in range(length-1):
            if cost_effectiveness[i] < cost_effectiveness[i+1]:
                inter = cost_effectiveness[i+1]
                cost_effectiveness[i+1] = cost_effectiveness[i]
                cost_effectiveness[i] = inter
                inter = positions2[i+1]
                positions2[i+1] = positions2[i]
                positions2[i] = inter
                next_pass = True

    effective_solutions = []
    for i in range(length):
        if cost_effectiveness[i] == cost_effectiveness[0]:
            effective_solutions.append(positions2[i])

    print('')
    print('Total number of solutions tested:', length)
    print('Heighest score obtained:', scores[0])
    print('Solution(s) with highest score', high_score_solutions)
    print('Most cost effective solution(s)', effective_solutions)
    print('')
    print('Top', palmares, 'Bubble Solutions (in score):', )
    for i in range(palmares):
        number_sign = str(i+1)+")"
        position = "#"+str(positions[i])
        print(number_sign, 'Bubble solution', position, 'score:', scores[i])


# real start of program
# verify that the lists match
scores_length = len(scores)
costs_length = len(costs)
if scores_length == costs_length:
    print("Verified : score list and cost list have the same number of items.")
    print('')
    length = scores_length
else:
    quit

# decide how long the palmares list will be
# data validation : length must be positive
# and no longer than the list
palmares = 0
while (palmares > length) or (palmares <= 0):
    palmares = int(input('Please enter the palmares size:   '))
print('')
print('At the end of the rapport')
print('you will receive a list of top', palmares, 'solutions.')
print('')


print_data()
print_rapport()

# Option 1 : sort the highest and put it away in a new list
# exclude the previous highest from sorting
# repeat this len times
# blocs : need to create a list of len elements and set all of them to zero
# needs two loops
# scores_sort = []
# for i in range(length):
#     scores_sort.append(0)

# for i in range(length-1):
#    if scores[i] > scores_sort[0]:
#        scores_sort[0] = scores[i]

# for n in range(length):
#    for i in range(length-1):
#        if (scores[i] > scores_sort[n]) and (scores[i] < scores_sort[n-1]):
#            scores_sort[n] = scores[i]

# below is the way to find the cost effective solution-s
# if cost effectiveness is redefined as
# having the lowest cost amongst those who produce
# the highest scores
# select_length = len(high_score_set)
# high_score_cost = 100
# effective_high = []
# for i in range(select_length):
#    if costs[high_score_set[i]]<= high_score_cost:
#        high_score_cost = costs[high_score_set[i]]
#        effective_high.append(high_score_set[i])
