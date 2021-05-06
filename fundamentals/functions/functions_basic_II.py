
# 1 ...............................................................

# Create a function that accepts a number as an input. Return a new list 
# that counts down by one, from the number (as the 0th element) down to 0 
# (as the last element).Example: countdown(5) should return [5,4,3,2,1,0]

def countdown(list_size):
    new_list=[]
    for i in range(list_size,-1,-1):
        new_list.append(i)
    return new_list
print(countdown(7))

# 2..............................................................................

# Create a function that will receive a list with two numbers. Print the first value 
#and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2

def print_and_return(numbers):
    print(numbers[0])
    return numbers[1]
print(print_and_return([8,15]))

# 3................................................................................

#Create a function that accepts a list and returns the sum of the first value in the 
#list plus the list's length.Example: first_plus_length([1,2,3,4,5]) should return 6 
#(first value: 1 + length: 5)

def my_add_function(nums):
    return len(nums) + nums[0]
print(my_add_function([2,6,8,4,9,8,4]))

# 4..................................................................................

#Values Greater than Second - Write a function that accepts a list and creates a new 
#list containing only the values from the original list that are greater than its 2nd 
#value. Print how many values this is and then return the new list. If the list has less 
#than 2 elements, have the function return False
#   Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
#   Example: values_greater_than_second([3]) should return False

def greater_than(sample):
    if len(sample)<2:
        return False
    else:
        brand_new_list=[]
        total=0
        for i in range(0,len(sample)):
            if sample[i]>sample[1]:
                total +=1
                brand_new_list.append(sample[i])
        print(total)
        return brand_new_list

print(greater_than([10,5,8,20,2,7,9]))

# Write a function that accepts two integers as parameters: size and value. 
# The function should create and return a list whose length is equal to the 
# given size, and whose values are all the given value Example: length_and_value(4,7) 
# should return [7,7,7,7] 
#   Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def length_and_value(size,value):
    new_creation=[]
    for i in range(0,size):
        new_creation.append(value)
    return new_creation
print(length_and_value(5,4))






