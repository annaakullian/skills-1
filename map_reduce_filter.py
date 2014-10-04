number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]


square = lambda x: x**2

def my_map(function, list):
    squared = []
    for i in list:
        squared.append(function(i))
    return squared 

print my_map(square, number_list)

odd_num = lambda x: x % 2 != 0

def my_filter(function, list): 
    odds = [] 
    for i in list:
        if function(i):
            odds.append(i)
    return odds
print my_filter(odd_num, number_list)

summed = lambda x, y: x + y

def my_reduce(function, list):
    accumulator = list[0]
    for i in list[1:]:
        accumulator = function(accumulator, i)
    return accumulator

print my_reduce(summed, number_list)


