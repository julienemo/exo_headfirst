# import ch1text.py
# import doesn't work for i7 nor dell
# error msg:ImportError: No module  named 'ch1text.py'; 'ch1text' is not a package

# things to do
# 1 figure out why import doesn't work
# 2 separate the modules
# 3 get the syllable part done
# 4 forgot to push the last modifs from i7, occasion to test confict management
text = """The first thing that stands between you and writing your first, real,
piece of code, is learning the skill of breaking problems down into
acheivable little actions that a computer can do for you. Of course,
you and the computer will also need to be speaking a common language,
but we'll get to that topic in just a bit.

Now breaking problems down into a number of steps may sound a new
skill, but its actually something you do every day. Let’s look at an
example, a simple one: say you wanted to break the activity of fishing
down into a simple set of instructions that you could hand to a robot,
who would do your fishing for you. Here’s our first attempt to do that,
check it out:

You can think of these statements as a nice recipe for fishing. Like any
recipe, this one provides a set of steps, that when followed in order,
will produce some result or outcome in our case, hopefully, catching
some fish.

Notice that most steps consists of simple instruction, like "cast line
into pond", or "pull in the fish." But also notice that other
instructions are a bit different because they depend on a condition,
like “is the bobber above or below water?". Instructions might also
direct the flow of the recipe, like "if you haven’t finished fishing,
then cycle back to the beginning and put another worm on the hook."
Or, how about a condition for stopping, as in “if you’re done” then go
home.

You’re going to find these simple statements or instructions are the
first key to coding, in fact every App or software program you’ve ever
used has been nothing more than a (sometimes large) set of simple
instructions to the computer that tell it what to do. """


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
    # appro. syllable countings according to following principles
    # 1.when a word contains 3 letters or less=> 1 syllable
    prev_char_vow = False
    if len(word) <= 3:
        return 1

    # 2. otherwise, a word has so many syllables as the nb of vows
    # however, vow sequences are considered as only one vow
    count = 0
    vows = 'aeiouAEIOU'
    for char in word:
        if char in vows:
            if prev_char_vow == False:
                count = count + 1
            prev_char_vow = True
        else:
            prev_char_vow = False
    return count


def total_syllables(target_text):
    # logic : count syllables in each word then add together
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


display_text(text)
readability(text)
