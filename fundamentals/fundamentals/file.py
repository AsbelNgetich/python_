num1 = 42 # variable declaration, initialize number
num2 = 2.3 # variable declaration, initialize float
boolean = True # variable declaration, initialize boolean
string = 'Hello World' # variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}# variable declaration, initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana')# variable declaration, initialize Tuple
print(type(fruit))#type check
print(pizza_toppings[1]) #log statement,access value
pizza_toppings.append('Mushrooms') #add value to a list
print(person['name'])#log statement,access value
person['name'] = 'George' #change value
person['eye_color'] = 'blue' #change value
print(fruit[2])#log statement,access value



if num1 > 45:# conditional if statement checks if value greater than 45
    print("It's greater")# log statement
else: # conditional else
    print("It's lower")log statement

if len(string) < 5: # if statement
    print("It's a short word!") #log statement
elif len(string) > 15: #elseif statement
    print("It's a long word!") #log statement
else: #else
    print("Just right!") # log statement


for x in range(5): #for loop, starts from 0 to 4
    print(x) #log statement


for x in range(2,5): #for loop, starts from 2 to 4
    print(x) #log statement


for x in range(2,10,3): #for loop, starts from 2 to 9 with increments of 3
    print(x) # log statement


x = 0 # variable declarization and initialization
while(x < 5): # while loop with a condition. x less than 5
    print(x) # log statement
    x += 1 # x is incremented by 1

pizza_toppings.pop() #Delete value
pizza_toppings.pop(1) #Delete item at a specific index

print(person) # log statement
person.pop('eye_color') # Eelete specific item
print(person) # log statement

for topping in pizza_toppings: # for loop
    if topping == 'Pepperoni': #if statement
        continue # continue
    print('After 1st if statement') #log statement
    if topping == 'Olives': # if statement
        break #breaks out of the loop if condition is met

def print_hello_ten_times(): # function definition
    for num in range(10): # for loop
        print('Hello') #log statement

print_hello_ten_times() # functin call

def print_hello_x_times(x): # function definition with a parameter
    for num in range(x): # for loop
        print('Hello') # log statement

print_hello_x_times(4) # function call with arguments


""" function definition with, variable declaration
and initialization as a parameter """
def print_hello_x_or_ten_times(x = 10): 
    for num in range(x): #for loop
        print('Hello') #for loop

print_hello_x_or_ten_times() #function call
print_hello_x_or_ten_times(4) # fuction call with arguments


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)