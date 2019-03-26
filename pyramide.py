# wanted the user to choose between two stuffs
# given there are only two choices I thought of boolean
# for ex like this
# choice = bool(input('Would you wand a whole or half pyramid ?'))
# but it didn't work out coz True == having and answer and False == no answer


import sys


def get_choice():
    valid = {"WHOLE": True, "whole": True, "Whole": True, "W": True, "w": True,
             "HALF": False, "Half": False, "half": False, "H": False, "h": False}
    sys.stdout.write("Would you like your pyramid to be whole or half ? (answer w/h):    ")
    choice = input().lower()
    while choice not in valid:
        sys.stdout.write("Would you like your pyramid to be whole or half ? (answer w/h):    ")
        choice = input().lower()
    return valid[choice]


def get_n():
    print('How many floors do you want for your pyramid ?')
    n = input('Please enter positive interger less than 20     ')
    # look carefully
    # this is the data validation solution I've bee looking for
    # while True
    # try the logical thing (int(n) in a certain range)with a while then break
    # except the risk that can cause an error message (int(n)returns error is n is not number)
    # Then found the following,
    # don't understand yet
    # but works
    
    while True:
        try:
            while (int(n) <= 0) or (int(n) >= 20):
                print("I thought I said POSITIVE LESS THAN 20")
                n = input('Try harder and give me a good one     ')
            break
        except:
            print('I thought I said positive interger smaller than 20. AKA as I said')
            n = input('Try harder and give me a good one     ')
    print('-----')
    print('There it is....', n, 'is a good positive interger less than 20')
    print('-----')
    print('Here is your', n, 'floor pyramid.')
    print('')
    return int(n)


def prt_pyr():
    n = get_n()
    for i in range(n):
        print(' ' * (n - i - 1), "#" * (i + 1), "#" * (i + 1), ' ' * (n - i - 1) )


def prt_hfpyr():
    n = get_n()
    for i in range(n):
        print(' ' * (n - i - 1), "#" * (i + 1))


choice = get_choice()
if choice:
    prt_pyr()
else:
    prt_hfpyr()
