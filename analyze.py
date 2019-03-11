"""The analyze module uses Flesch-Kincaid readability test to analyze text and
produce a readability score. This score is then converted into a grade-based
readability category."""


def total_words(target_text):
    """This function counts the number of words in the text.
    It brakes the text into a list of items separated by white spaces.
    The items are bases of words. The length of the mentioned list
    is considered the number of words."""

    splited_text = target_text.split()
    nbwords = len(splited_text)
    return nbwords


def total_phrases(target_text):
    """This function counts the number of phrase.
    It actually counts the number of punctuations
    that delimite a phrase. Namely periods, semicolomn,
    exclamation and question marks."""

    nbphrase = 0
    separators = '.!?;'
    for char in target_text:
        if char in separators:
            nbphrase = nbphrase + 1
    return nbphrase


def word_syllables(word):
    """This function approximately counts the number
    of syllables in a single word.
    It is based on the following principles:
    1. the punctuations and silent e at the end are to be wiped
    2. words containing no more than 3 letters have only one syllable
    3. for words with +3 letters, one vowel is one syllable, unless preceeded by another
    4. for words with +3 letters, the letter Y at the end is considered a syllable"""

    count = 0
    endings = '!@#$%^&*()_+[]{}:;,.eE"'+"'"

    while word[-1] in endings:
        word = word[: -1]

    if len(word) <= 3:
        return 1

    vows = 'aeiouAEIOU'
    prev_char_vow = False
    for char in word:
        if char in vows:
            if not prev_char_vow:
                count = count + 1
            prev_char_vow = True
        else:
            prev_char_vow = False

    if word[-1] in 'Yy':
        count = count + 1

    return count


def total_syllables(target_text):
    """This function simply goes through every item in the list
    of splited text and add the number of syllables of each word."""

    splited_text = target_text.split()
    count = 0
    for word in splited_text:
        count = count + word_syllables(word)
    return count


def readability(target_text):
    """This function takes the number of words, phrases and
    syllables in a text with the help of three previous functions
    (total_words, total_phrases and total_syllables) and compute
    the score according to Flesch-Kincaid method and indicates
    the corresponding level of study necessary to understand the text.
    It displays the three number together with the score
    as well as the level."""

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
    """This function displays the analyzed text."""

    print('Text to analyze:')
    print('')
    print('-------TEXT BELOW-------')
    print(target_text)
    print('-------TEXT ENDS-------')
    print('')


def result(target_text):
    """This function produces a comprehensive report,
    including the three indicators, the score and the level."""

    display_text(target_text)
    readability(target_text)


if __name__ == '__main__':
    import ch1text
    result(ch1text.text)
