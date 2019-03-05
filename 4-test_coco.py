smoothies = ['coconut', 'strawberry', 'banana', 'tropical', 'acai berry']

has_coconut = [True, False, False, True, False]

length = len(smoothies)

for i in range(length):
    if has_coconut[i] is True:
        print(smoothies[i], 'contains coconut.')
