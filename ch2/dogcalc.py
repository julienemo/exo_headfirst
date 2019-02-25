# The program asks the user name and age
# of his or her dog
# Then returns a phrase Your dogXX's human age is XX

# At the end of each prompt, a space is include
# So that the answer does not stay attached
# to the question

# Also given there is a single quote in the string
# The string is deliminated by double strings

prompt_name = "What is your dog's name ? "
name = input(prompt_name)

prompt_age = "What is your dog's age ? "
age = input(prompt_age)

human_age = int(age) * 7

print('Your dog', name, 'is', human_age, 'years old in human age.')
# see concatenating with coma instead of plus sign
# allows putting together stuffs without involving operation
# thus allowing concatenation between strings and numbers
# it takes less space and reduces convertion
