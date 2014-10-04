number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

def all_odd(number_list):
    return [i for i in number_list if i % 2 != 0]
print all_odd(number_list)

def all_even(number_list):
    return [i for i in number_list if i % 2 ==0]
print all_even(number_list)

def long_words(word_list):
    return [i for i in word_list if len(i) > 3]
print long_words(word_list)

def halvesies(number_list):
    return [i/2.0 for i in number_list] 
print halvesies (number_list)

def word_lengths(word_list):
    return [len(i) for i in word_list]
print word_lengths(word_list)

