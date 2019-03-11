# import ch1text.py
# import doesn't work for i7, to be tested on dell
# error msg:ImportError: No module  named 'ch1text.py'; 'ch1text' is not a package

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

def compute_readability(target_text):  # separated fun to count and calculate
    # Counting words. word = whatever is separted by white space
    words = target_text.split()
    total_word = len(words)

    # Counting phrases. phrase = whatever is separated by one item in the following list
    separators = '.!?;'
    # instead of using if char == blablabla
    # or if char in []
    total_phrase = 0
    for char in target_text:
        if char in separators:
                total_phrase = total_phrase + 1


    total_syllable = 0
    # score = 206.835 - 1.015 * (total_word / total_phrase) - 84.6 * (total_syllable / total_word)
    print('Text to analyze:')
    print('')
    print(text)
    print('')
    print('Total words:', total_word)
    print('Total phrases:', total_phrase)
    print('Total syllables:',total_syllable)
    # print('Readability score:',score)


def readability_level(readability_score):
    a = readability_score
    text = "Reading level of"
    if a > 90:
        l = '5th Grade'
    elif a > 80:
        l = '6th Grade'
    elif a > 70:
        l = '7th Grade'
    elif a > 60:
        l = '8-9th Grade'
    elif a > 50:
        l = '10-12th Grade'
    elif a > 30:
        l = 'College student'
    else:
        l = 'Gollege Graduate'
    print(text, l)

compute_readability(text)
readability_level(85)
