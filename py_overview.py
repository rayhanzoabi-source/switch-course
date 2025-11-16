# name of var can be anything (except saved words).
import random
y = 2
type = 3  # no no no!
# what else? str, dict

# python is dynamically typed: variables have no type
no_type = 66
no_type = "now I am a string"

# use meaningful names
# convetion - separate words with lodash
num_of_books = 2

# Basic types
integer = 4
floating_point = 3.4
complex_number = 2 + 3j

string = "hello"
boolean = True


# mathematical operators: + - * /
# use parenthesis in math
a = 2
b = 5
(a + b) * 2

# modulo
remaining = 3 % 2

# ** exponent,
exp = 5 ** 2

# floor division
rounded_res = 7//3

# logical operators: and or not
a and b

# concatenation
print("Hello " + "world")

# concatenation with numbers
print(str(24) + " hours a day")

# ######## errors 

# runtime errors
# Type error
print(2 + " days")

# logical errors. harder to find
x = 5
# add 10 to x
x + 10
if x > 10:
    print("x > 10")


# conditions
x = 5

if x > 2:
    print("x is greater than 2")
elif x == 2:
    print("x = 2")
else:
    print("x is smaller than 2")

# code block

if True:
    y = 2
    y += 1
    print(y)


# ternary:
import random

num = random.randint(1, 100)

if num > 80:
    print("num > 80")
else:
    print("num <= 80")

message = "num > 80" if num > 80 else "num <= 80"
print(message)

# lists
# create a list
nums = [2, 4, 8, 16]

# list comprehension
same = [x for x in nums]
odds = [x + 1 for x in nums]
big_odds = [num + 1 for num in nums if num > 5]

# how to initialize list with 10 zeros?
# 1
size = 10
zeros = [0] * size
# 2: list comprehension
zeros = [0 for _ in range(10)]


# can use an expression as the index
index = 0
nums[index + 1]

# add new item
nums.append(32)

# check if item is in the list
print(4 in nums)  # what is the runtime?

# remove, what is the run time?
nums.remove(4)

# remove by index
nums.pop(1)
# remove the last one
print(nums.pop())

# pass by reference
list1 = [1, 2]
list2 = list1
list2.remove(2)
print(list1)

# access negative index
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
last = numbers[-1]
print(last)

# slicing
start = 1  # inclusive
end = 8  # non inclusive
step = 2

print(numbers[start:end:step])
# start > end (in actual indexes, not considering minuses)


# defaults are: start = 0, end = len(iter)
# when using -1 for the step argument, the direction is reversed.
# The start is still the start (default  = -1).
# and for end is (0 inclusive - can't be written, the beginning of the array)

print(nums[-1::-1])  # same as nums[::-1]
print(nums[::-1])

# nums[start_i:end:-1];
# start from start_i go each time left (towards the begining)
# until you reach the end

# slice assignment: allows you to replace part of the seq with new items
nums = [1, 2, 3, 4]
nums[1] = 20  # simple assignment
nums[1:3] = [20, 30]  # slice assignment
print(nums)

#### strings

# len

word = "pomelo"
len(word)  # not just for lists

# duplicate string

x = "foo"
print(x * 2)

# split
sentence = "day and night"
print(sentence.split(" "))

# join
delimiter = '-'
print(delimiter.join(['W', 'O', 'W']))

# indexes
print("Choclate"[2])

# format
score = 100
greeting = f"My score is {score}"
print(greeting)


# loops
# iteration: for in

# print all elements in a list
names = ["Amy", "Tammy", "Samy"]

for name in names:
    print(name)

# iterate indexes, in range
nums = [0, 13, 22, 48]
# print numbers in odd indices 1,3,5...

for i in range(0, len(nums)):
    if i % 2 == 1:
        print(nums[i])

# or
for i in range(1, len(nums), 2):
    print(nums[i])


for index, val in enumerate(nums):
    print(f"index = {index}, val = {val}")

# while
sum = 0
while sum < 8:
    sum += 2

# functions
def printInfo(name, last_name, age):
    print("I am " + name + " " + last_name +
          " and I am " + str(age) + " years old")


printInfo("Adam", "Biton", 43)
printInfo("Levana", "Biton", 44)


# dictionaries
# syntax

user = {
    "username": "nomonim",
    "age": 23,
    "isVip": False,
    "completed_levels": [2, 3, 5]
}

# updating and access property
user["age"] = 24
print(user["age"])
print(user.age)  # AttributeError

# what is the problem?
if user["id"] > 3:
    print("id > 3")  # exception, solve with get or check with in

# solution 1
if "id" in user and user["id"] > 3:
    print("id > 3")

# using get()
d = {}

# when using get() with a key that is absent from the dictionary, we will get None.
d.get("paris")  # None

# If we do it with brackets, an exception will be thrown
d["paris"]  # Error

# you can pass a default value
d.get("China", "Beijing")

# solution 2
if user.get("id") and user.get("id") > 3:
    print("id > 3")

# solution 3
if user.get("id", -1) > 3:
    print("id > 3")


# using variables as keys

key = "age"
print(user[key])

# what is it good for? getting data from a file/user input and use it dynamically


# nested dicts

user2 = {
    "username": "romeo",
    "age": 33,
    "isVip": True,
    "completed_levels": [1, 2, 3, 4, 5],
    "friend": {
        "username": "gomez",
        "age": 43,
        "isVip": False,
        "completed_levels": [1, 2]
    }
}

# how do we access the username of user2 friend?


# or in 2 steps


# pass by reference
friend = {
    "username": "gomez",
    "age": 43,
    "isVip": False,
    "completed_levels": [1, 2]
}

super_user = friend
super_user["age"] = 44
print(friend["age"])


# dict comprehension
first_letters = {x: x[0] for x in ["hello", "foo", "dada"]}

# interpreted: will throw exception only when it reaches the line
x = 4
x += 9
print(f"x = {x}")
x = x / 0
print("finished")

# io

number = input("enter a number\n")
if int(number) > 5:
    print("your number is bigger than 5")
else:
    print("your number is smaller or equal to 5")


# CPython implementation detail: the id is the address of the object in memory.
x = "hello"
print("x id ", id(x))

# mutable
x = [1,2,3]
copy = x
x += [4] # changing the list
print(x, copy)
print("id(x) == id(copy):", id(x) == id(copy))

# immutable
y = (1,2,3)
copy = y
y += (4,) # creating a new tuple
print(y, copy)
print("id(y) == id(copy):", id(y) == id(copy))


# mutable
print("**           Dicts           **")
a = {"a": 1, "b": 2}
b = {"a": 1, "b": 2}
print("a == b ", a == b) # true
print("a is b", a is b) # false
print("a id: ", id(a))
print("b id: ", id(b))

# immutable
print("**           strings           **")
a = "always the same"
b = "always the same"
print("a == b ", a == b) # true
print("a is b", a == b) # true
print("a id: ", id(a))
print("b id: ", id(b))

user = {
    "username": "nomonim",
    "age": 23,
    "isVip": False,
    "completed_levels": [2, 3, 5]
}

def print_id(user):
    user_id = user.get("id", 0)
    if user["id"] > 3:
        print("id > 3")

print_id(user)