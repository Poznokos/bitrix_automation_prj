from random_word import RandomWords
words = RandomWords()


def word_generator(count=1):
    words_list = ''
    for i in range(count+1):
        words_list += (words.get_random_word() + ' ')
    return words_list.rstrip()
