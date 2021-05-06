
# 4Create a function printInfo(some_dict) that given a dictionary whose values are 
# all lists, prints the name of each key along with the size of its list, and then
# prints the associated values within each key's list

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
 
def printInfo(some_dict):
    
    for key in some_dict:
        n= len(some_dict[key])
        
        print(n, key, some_dict[key])

printInfo(dojo)
       