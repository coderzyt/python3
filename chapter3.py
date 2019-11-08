def read_txt_from_file(file):
    return file


def read_txt(text):
    read_list = text.split()
    dic = {}
    for every_word in read_list:
        if dic.__contains__(every_word):
            dic[every_word] += 1
        else:
            dic.setdefault(every_word, 1)
    print(dic)

def test_cmp(stext, dtext):
    cmplist = []
    slineslist = []


def getAll(*args):
    print(args)

def getAlls(**args):
    print(args)

def funexe(keyparam, choice=1, *args, **keywords):
    print(keyparam, choice, args, keywords)

f = lambda a: (a and 1 or 2)


if __name__ == '__main__':
    # text = 'test test deploy compile return of the king king king'
    # read_txt(text)
    # getAll(1)
    # getAll(1, 2)
    #
    # getAlls(one=1)
    # getAlls(one=1, two=2)
    # funexe('a', 'b', 'c', 'd')
    # funexe('a', 1, 'c', 'd')
    # funexe('a', 1, 'c', 'd', three=3)

    print(f(False))
