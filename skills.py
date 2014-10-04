number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

def all_odd(number_list):
    odd_list = []
    for num in number_list:
        if num % 2 != 0:
            odd_list.append(num)
    return odd_list
#print all_odd(number_list)

def all_even(number_list):
    even_list = []
    for num in number_list:
        if num % 2 == 0:
            even_list.append(num)
    return even_list
#print all_even(number_list)

def long_words(word_list):
    long_word = []
    for word in word_list:
        if len(word)>3:
            long_word.append(word)
    return long_word
#print long_words(word_list)

def smallest(number_list):
    smallest = number_list[0]
    for i in range(1, len(number_list)):
        if smallest < number_list[i]:
            smallest = smallest
        else:
            smallest = number_list[i]
    return smallest
#print smallest(number_list)

def largest(number_list):
    largest = number_list[0]
    for i in range(1, len(number_list)):
        if largest<number_list[i]:
            largest = number_list[i]
    return largest
#print largest(number_list)

def halvesies(number_list):
    halves = []
    for num in number_list:
        halves.append(num/2.0)
    return halves
#print halvesies (number_list)

def word_lengths(word_list):
    lengths = []
    for word in word_list:
        lengths.append(len(word))
    return lengths
#print word_lengths(word_list)

def sum_numbers(number_list):
    summ = 0
    for num in number_list:
        summ += num
    return summ
print sum_numbers(number_list)

def mult_numbers(number_list):
    product = 1
    for num in number_list:
        product = product*num
    return product
print mult_numbers(number_list)

def join_strings(word_list):
    string = ""
    for word in word_list:
        string = string + word + " "
    return string
print join_strings(word_list)

def average(number_list):
    num_of_nums = len(number_list)
    average = sum_numbers(number_list)/num_of_nums
    return average
print average(number_list)