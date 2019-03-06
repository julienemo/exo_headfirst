import ch1text
# import by typing only the name of the file without the .py


def total_words(target_text):
    # definition of word:
    # whatever is separated by a white space
    splited_text = target_text.split()
    nbwords = len(splited_text)
    return nbwords


def total_phrases(target_text):
    # definition of phrase:
    # whatever is separated by .!?;
    nbphrase = 0
    separators = '.!?;'
    for char in target_text:
        if char in separators:
            nbphrase = nbphrase + 1
    return nbphrase


def word_syllables(word):
    # counting syllables in each word
    count = 0

    # cleaning words
    # getting rid of any slient e or punts at the endings
    # there needs to be several passes
    endings = '!@#$%^&*()_+[]{}:;,.eE"'+"'"
    while word[-1] in endings:
        word = word[: -1]
    # if a clean word has no more than 3 letters
    # there is only one syllable
    if len(word) <= 3:
        return 1
        # here reture instead of count
        # other wise the rest of the code will add syllables

    # for words with more than 3 letters
    # any vowel is one syllable, unless preceeded by another
    vows = 'aeiouAEIOU'
    prev_char_vow = False
    for char in word:
        if char in vows:
            if not prev_char_vow:
                count = count + 1
            prev_char_vow = True
        else:
            prev_char_vow = False

    # for words with more than 3 letters
    # y at the end of a word considered vow aka syllable
    if word[-1] in 'Yy':
        count = count + 1

    return count


def total_syllables(target_text):
    # logic : count syllables in each word then
    splited_text = target_text.split()
    count = 0
    for word in splited_text:
        count = count + word_syllables(word)
    return count


def readability(target_text):
    nb1 = total_words(target_text)
    nb2 = total_phrases(target_text)
    nb3 = total_syllables(target_text)
    k1 = 206.835
    k2 = 1.015
    k3 = 84.6
    score = round((k1 - k2 * (nb1 / nb2) - k3 * (nb3 / nb1)), 2)

    print_text = "Reading level of"
    if score > 90:
        level = '5th Grade'
    elif score > 80:
        level = '6th Grade'
    elif score > 70:
        level = '7th Grade'
    elif score > 60:
        level = '8-9th Grade'
    elif score > 50:
        level = '10-12th Grade'
    elif score > 30:
        level = 'College student'
    else:
        level = 'Gollege Graduate'

    print('Total words:', nb1)
    print('Total phrases:', nb2)
    print('Total syllables:', nb3)
    print('')
    print('Readability score:', score)
    print(print_text, level)


def display_text(target_text):
    print('Text to analyze:')
    print('')
    print('-------TEXT BELOW-------')
    print(target_text)
    print('-------TEXT ENDS-------')
    print('')


def result(target_text):
    display_text(target_text)
    readability(target_text)


result(ch1text.text)
