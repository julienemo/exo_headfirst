def word_syllables(word):
    count = 0
    # appro. syllable countings according to following principles

    # 0.get rid of any punctuation or Ee at the end of a word
    endings = '!?:;,."+-/=()[]@#$%^&*eE'+"'"
    if word[-1] in endings:
        word = word[: -1]

    # 1.when a word contains 3 letters or less=> 1 syllable
    prev_char_vow = False
    if len(word) <= 3:
        return 1

    # 2. otherwise, a word has so many syllables as the nb of vows
    # however, vow sequences are considered as only one vow
    vows = 'aeiouAEIOU'
    for char in word:
        if char in vows:
            if prev_char_vow == False:
                count = count + 1
            prev_char_vow = True
        else:
            prev_char_vow = False

    # 3. ending y is considered to be vows
        if (word[-1] in 'yY') and (len(word) > 3):
            count = count + 1
    return count
