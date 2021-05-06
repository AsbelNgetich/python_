#1  This function returns a 5 that gets printed on the screen
def number_of_food_groups():
    return 5
print(number_of_food_groups())

#2  prints an error because the 1st function is not defined 
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())

#3 prints 5 because you can only have one return statement in a function. The value
# of the first return statement is returned and the rest is skipped.
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())

#4 Prints 5 because once the program executes the return statement, the rest 
# of the statements in that function are skipped.
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())

#5 Prints 5 then none because when the function gets called on line 28 it prints
# then number 5 but it doesnt have a return statement. So nothing gets assigned to 
# the variable x since nothing is being returned
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)

#6 Throws and error because add function isn't returning values that could be added in 
# the print statement
def add(b,c):
    print(b+c)

print(add(1,2) + add(2,3))

#7 Prints 25 because it casts the numbers to a string and concatenates them
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))

#8 Prints the value of b then returns 10 because b is greater than 10
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())

#9 Prints 7 then 14 then 21
# b is less than c, so it returns 7
# b is greater than c so it returns 21
# The last statement adds the returned values
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))

#10 Prints 8 because it returns the sum of the two values
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))

#11 This code would give an error because in line 80  a string is being compared to a number
# if it were correct syntax, the print out would have been 500 500 True or false 500
# because the variable b in the function foobar() would have been assigned a boolean value
# its also only local in foobar
b = 500
print(b)
def foobar():
    b = True # "keyword operator from-rainbow">= 300
    print(b)
print(b)
foobar()
print(b)

#12 Prints 500 500 300 500 foobar() returns the 300 but doesnt get assigned to anything
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)

#13 Prints 500 500 300 300 foobar() returns the 300 but doesnt get assigned to b
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)

#14 Prints 1 then calls on bar() which prints 3  then continues to print 2
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()

#15 prints 1 then calls bar()-which prints 3 and returns 5. which is then printed
# and returns 10 that's assigned to y and printed
#1 3 5 10
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)