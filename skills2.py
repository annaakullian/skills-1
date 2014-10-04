number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

def all_odd(number_list):
    return list(filter(lambda x: x % 2 != 0, number_list))
print all_odd(number_list)

def all_even(number_list):
    return list(filter((lambda x: x% 2 == 0), number_list))
print all_even(number_list)

def long_words(word_list):
    return filter((lambda x: len(x)>3), word_list)
print long_words(word_list)

def smallest(number_list):
    return reduce(lambda a,b: a if a < b else b, number_list)
print smallest(number_list)

def largest(number_list):
    return reduce(lambda a,b: a if a > b else b, number_list)
print largest(number_list)

def halvesies(number_list):
    return map(lambda x: x/2.0, number_list)
print halvesies (number_list)

def word_lengths(word_list):
    return map(lambda x: len(x), word_list)
print word_lengths(word_list)

def sum_numbers(number_list):
    return reduce(lambda x, y: x + y, number_list)
print sum_numbers(number_list)

def mult_numbers(number_list):
    return reduce(lambda x, y: x*y, number_list)
print mult_numbers(number_list)

def join_strings(word_list):
    return reduce(lambda x, y: x + " " + y, word_list)
print join_strings(word_list)

def average(number_list):
    return sum_numbers(number_list)/len(number_list)
print average(number_list)