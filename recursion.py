number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

square = lambda x: x**2

def my_map(function, list):
    if list == []:
        return list 
    else:
        # return [function(list[0])].append(my_map(function, list[1:]))
        return [ function(list[0]) ] + my_map(function, list[1:])


print my_map(square, number_list)


odd_num = lambda x: x % 2 != 0

def my_filter(function, list):
    if list == []:
        return list
    else:
        if function(list[0]):
            return [ list[0] ] + my_filter(function, list[1:])
        else:
            return my_filter(function, list[1:])

print my_filter(odd_num, number_list)


summed = lambda x, y: x + y

def my_reduce(function, list):
    if len(list) == 1:
        return list[0]
    elif list == []:
        return 0   
    else:
        return function(list[0], (my_reduce(function, list[1:])))

print my_reduce(summed, number_list)


