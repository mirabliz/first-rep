

def add(n1, n2):
    return n1 + n2


def sutract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculator(operation, n1, n2):
    return operation(n1, n2)


result = calculator(multiply, 10, 20)
print(result)
print(calculator(add, 15, 20))
print(calculator(divide, 64, 4))

def calculator(operation, n1, n2):
    return operation(n1, n2)

result = calculator(lambda n1, n2: n1 + n2, 5, 15)
print(result)

num_list = [1, 2, 3, 4, 5, 6]
double_list = map(lambda n: n * 2, num_list)
print(list(double_list))

num_list = [-1, 21, -3, 40, 115, -76]
my_list = list(filter(lambda n : n >10, num_list))
print(my_list)

num = 30

def multiply_by_10(n):
    n *= 10
    num = n
    print("Value of num inside function:", num)
    return n

multiply_by_10(num)
print(" Value of num inside function:", num)

random_string = "This is my phone in the hub"
print(random_string.find("is", 8, 13))


_string = "Welcome to my world"
print(_string.replace("world", "home"))
print(_string.upper())

list = ("a", "b", "c")
print(">>" .join(list))
print(":" .join(list))

string1 = "learn python {version} at {name}".format(version = 3, name = "educative")
string2 = "Leran python {0} at {1}".format(3, "Educative")
print(string1)
print(string2)
num = lambda n : n * 3
print(num(10))

concate_strings = lambda a, b, c : a[0] + b[0] + c[0]
print(concate_strings("World", "Wide", "Web"))
just_ = lambda num: "higher" if num > 50 else "lower"
print(just_(70))

def multiply(n1, n2):
    return n1 * n2

def calculator(operation, n1, n2):
    return operation(n1, n2)

result = calculator(multiply, 10, 30)
print(result)
results = calculator(lambda n1, n2 : n1 + n2, 20, 50)
print(results)

def rec_count(number):
    print(number)
    if number == 0:
        return 0
    rec_count(number - 2)
    print(number)

rec_count(10)

my_string = "Hello World"


def exclamation(my_string):
    my_string = "!!" + my_string + "!!"
    return(my_string)

exclamation(my_string)
print(my_string)



x = 3
y = 4

def rep_cat(x, y):
    return str(x) * 10 + str(y) * 5

print(rep_cat(x, y))
# print(rep_cat)

def factorial(n):
    if n == 0 or n == 1:
        return 1


    if n < 0:
        return -1


    return n * factorial(n - 1)
print(factorial(5))



for i in range(1, 11):
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")


for i in range(1, 11, 3):
    print(i)


float_list = [2.5, 16.55, 50.2, 12.44, 40.5]
print(float_list)

for i in range(0, len(float_list)):
    float_list[i] = float_list [i] * 2

print(float_list)


float_list = [2.5, 16.55, 50.2, 12.44, 40.5, 11.0, 5.0]  
count_greater = 0

for num in float_list:
    if num > 10:
        count_greater += 1
print(count_greater)

n = 50
num_list = [10, 25, 4, 23, 6, 18, 27, 47]

for n1 in num_list:
    for n2 in num_list:
        if (n1 != n2):
            if(n1 + n2 == n):
                print(n1, n2)


# n = 50
# num_list =[10, 25, 4, 23, 6, 18, 27, 47]
# found = False

# for n1 in num_list:
#     for n2 in num_list:
#         if (n1 != n2):
#             if (n1 + n2 == n):
#                 found = True
#                 break
#     if found:
#         print(n1, n2)
#         break

num_list = range(20)
if num in num_list:
    pass
print(len(num_list))

num_list = range(0,10)
for num in num_list:
    if num == 3 or num == 6 or num == 8:
        continue
    print(num)


    n = 2
    power = 0 
    val = n
    while val <1000:
        power += 1
        val *= n
        print(power)


string_list = ["Anakin", "Luke", "Rey", "Leia", "Vader"]
for s in string_list:
    if len(s) <5:
        print(len(s))