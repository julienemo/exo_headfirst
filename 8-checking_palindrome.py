# test whether a word is palindrome
# works only without punctuation nor space


def test_if_palindrome(target):
    if len(target) <= 1:
        return True
    else:
        if target[0] == target[-1]:
            return test_if_palindrome(target[1:-1])
        else:
            return False


def test_if_palindrome_ite(target):
    if (target[::-1]) == target:
        # the [x:y:z] format means taking a list or a string from item x to item y
        # and at a pace of z
        if_pal = True
    else:
        if_pal = False
    print(if_pal)


str_to_test = input('Give a one-word-lowwer-case string.     ')
test_if_palindrome_ite(str_to_test)
