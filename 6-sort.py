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

# Option 1 : sort the highest and put it away in a new list
# exclude the previous highest from sorting
# repeat this len times
# blocs : need to create a list of len elements and set all of them to zero
# needs two loops
scores_sort = []
for i in range(length):
    scores_sort.append(0)

for i in range(length-1):
    if scores[i] > scores_sort[0]:
        scores_sort[0] = scores[i]

for n in range(length):
    for i in range(length-1):
        if (scores[i] > scores_sort[n]) and (scores[i] <= scores_sort[n-1]):
            scores_sort[n] = scores[i]

print('original', scores)
print('option1', scores_sort)

# option 2 : bublle sorting
# compare each item with the item after and itirate only once
# if n > n+1, swap with an intermediary
# bloc: how to repeat ?

inter = 0

next_pass = True

while next_pass is True:
    next_pass = False
    for i in range(length-1):
        if scores[i] < scores[i+1]:
            inter = scores[i+1]
            scores[i+1] = scores[i]
            scores[i] = inter
            next_pass = True

print('option2', scores)
