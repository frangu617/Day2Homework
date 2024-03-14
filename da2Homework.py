def max_num(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
print('Here are some numbers for max_num: 2, 3, 4')
print(f'The max number is {max_num(2, 3, 4)}') #max_num(2, 3, 4)


def mult_list(num_list):
    result = 1
    for num in num_list:
        result = result * num
    return result

numbers = [1, 2, 3]
print('the result of mult_list([1, 2, 3]) is',mult_list(numbers))


def rev_string(my_str):
    return my_str[::-1]

string_to_reverse = 'Here is a string to reverese -'
print(string_to_reverse,rev_string(string_to_reverse))

def num_within(x, a, b):
    return x in range(a, b + 1)
    
x = 5
a = 2
b = 4

print(f'is {x} between {a} and {b}?',num_within(3, 2, 4))

def pascal(n):
    row = [1]
    y = [0]
    for x in range(n):
        print(row)
        row = [left + right for left, right in zip(row + y, y + row)]
        


n = int(input('Enter a number for pascal triangle, keep in mind that it should not be a large number or it will take too long: '))

pascal(n)
