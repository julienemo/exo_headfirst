# there are several bubble solutions to evaluate
# Below is a list of their "scores" achieved
scores = [60, 50, 60, 58, 54, 54,
    58, 50, 52, 54,48, 69,
    34, 55, 51, 52, 44, 51,
    69, 64, 66, 55, 52, 61,
    46, 31, 57, 52, 44, 18,
    41, 53, 55, 61, 51, 44]

# and their cost
costs = [.25, .27, .25, .25, .25, .25,
    .33, .31, .25, .29, .27, .22,
    .31, .25, .25, .33, .21, .25,
    .25, .25, .28, .25, .24, .22,
    .20, .25, .30, .25, .24, .25,
    .25, .25, .27, .25, .26, .29]

# things to do
# 1.print the phrase "Bubble solution n X, score N" for each solutions
# 2.print the number of solutions tested
# 3.print the highest score achieved in the tests
# 4.print the index of solution(s) having achieved the highest score
# 5.print the index of solution(s) with highest cost cost_effectiveness
# cost effectiveness = producing high score with low cost


scores_length = len(scores)
costs_length = len(costs)

# verify that the lists match
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

# print the list
for i in range(length):
    number_sign = "#"+str(i)
    print('Bubble solution', number_sign, 'score: ', scores[i])

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

# option 2 : bublle sorting
# compare each item with the next
# if wrong order, switch (switch means set next_pass = True)

next_pass = True
positions = list(range(length))


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

print('')
print('Total number of solutions tested:', length)

high_score_solutions =[]
for i in range(length):
    if scores[i] == scores[0]:
        high_score_solutions.append(positions[i])

print('Heighest score obtained:', scores[0])
print('Solution(s) with highest score', high_score_solutions)
print('')
print('Top Bubble Solutions:')

for i in range(palmares):
    number_sign = str(i)+")"
    position = "#"+str(positions[i])
    print(number_sign, 'Bubble solution', position, 'score:', scores[i])
