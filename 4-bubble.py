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

highest_score = 0
# print scores and get highest score
for i in range(length):
    print('Bubbles solution #' + str(i+1), 'score:', scores[i])  # print score
    if scores[i] > highest_score:
        highest_score = scores[i]  # stock high score value

# get the index of solutions of which the scores
# corresponding to the high score
# if there are multiple solutions we take all in a list


high_score_set = []

for i in range(length):
    if scores[i] == highest_score:
        high_score_set.append(i)

# calculate cost effectiveness of each solution
# and store in a list
cost_effectiveness = []

for i in range(length):
    cost_effectiveness.append(scores[i] / costs[i])

# get the max of cost effectiveness
most_effective = 0

for i in range(length):
    if cost_effectiveness[i] > most_effective:
        most_effective = cost_effectiveness[i]

# get the index of solution(s) with the greatest effectiveness
effective_solutions = []

for i in range(length):
    if cost_effectiveness[i] == most_effective:
        effective_solutions.append(i)

print('')
print('Bubbles tests: ', length)
print('Highest bubble score: ', highest_score)
print('Solution(s) with highest score: ', high_score_set)
print('Solution(s) with highest effectiveness ', effective_solutions)

# below is the way to find the cost effective solution-s
# if cost effectiveness is redefined as
# having the lowest cost amongst those who produce
# the highest scores
select_length = len(high_score_set)
high_score_cost = 100
effective_high = []
for i in range(select_length):
    if costs[high_score_set[i]]<= high_score_cost:
        high_score_cost = costs[high_score_set[i]]
        effective_high.append(high_score_set[i])
