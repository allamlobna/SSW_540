'''Your code should populate 
an array with a list of object names. Object names can 
exist in pairs or non-pairs. Now your code should play the 
game of discovering any unique objects. Unique objects are 
objects that exist only once in the array. If an object 
is mentioned more than once (i.e. twice or more), it is not a unique object. '''


LIST_NAMES = ['tim', 'tim', 'lily', 'sam', 'john', 'john', 'kerry', 'bob', 'kerry', 'jessica']
TEST_2 = ['E']
TEST_3 = [5, 6, 7, 4, 3, 2, 2, 1, 6]
TEST_4 = ['a', 'b', 'b', 'b', 'c','d','e']
TEST_5 = []

def find_unique(string_names: list):
    '''finds unique values in a list and prints the list of unique values'''
    unique_list = []
    # use filter function to count all elements in list and lambda removes any values that appear more than once
    unique_list = list(filter(lambda s: string_names.count(s) < 2, string_names))                        
    return unique_list
            

if __name__ == '__main__':
    '''find unique strings in a pre-populated list'''
    print('This is the original array with a list of object names \n' + str(LIST_NAMES))
    print('These are the unique object names in the list \n' + str(find_unique(LIST_NAMES)))