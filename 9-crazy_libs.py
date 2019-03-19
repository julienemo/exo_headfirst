holders = ['NOUN', 'VERB', 'ADJECTIVE', 'VERB_ING']


def get_modif_phrase(phrase):
    global holders
    modif_phrase = ''
    phrase = phrase.split()
    # 这需要一个list
    # 因为后边要对一个一个的词进行判断甚至修改
    # list才可修改 string不可修改
    for word in phrase:
        if word in holders:
            word = input('Please give me a ' + word + ":    ")
            modif_phrase = modif_phrase + word + ' '
        elif word[:-1] in holders:
            word = input('Please give me a ' + word[:-1] + ":    ")
            modif_phrase = modif_phrase + word + ' '
        else:
            word = word
            modif_phrase = modif_phrase + word + ' '
    return modif_phrase + '\n'
    # takeaway是千万不能忘了空格和换行符号
    # 不然……会粘成一团浆糊><


def make_crazy_lib(target_file):
    try:
        the_file = open(target_file, 'r')
        # 在这打开它是为了里边调用的get_modif_phrase用的
        # 主func的确没有用到它的地方
        # 一开始不是把它放这的一开始是放global的
    except FileNotFoundError:
        print("Oups, didn't find this file. You sure ?")
    else:
        modif_text = ''
        # 这里并没有用到read功能
        # 那read到底有啥用    0 ^ o
        for phrase in the_file:
            modif_text = modif_text + get_modif_phrase(phrase)
        print("")
        print("-----HERE IS YOUR TEXT-----")
        print(modif_text)
        the_file.close()


make_crazy_lib('lib.txt')
# bizarre that I had to put quotation around the filename...
# 替换的套路：
# new_ensemble = ''
# for unit in ensemble:
#   new_ensemble = new_ensemble + unit + separator
#   return new_ensemble
