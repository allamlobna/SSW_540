'''Counting unique objects 
Following the same code you developed last week. 
All you need to do is to list ALL unique objects, 
and to count the number of unique objects.'''


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
    num_unique = len(unique_list)                        
    return unique_list, num_unique
            

if __name__ == '__main__':
    '''find unique strings in a pre-populated list'''
    #populate an array with a list of object names
    list_of_objects = LIST_NAMES
    print('This is the original list with a list of object names \n' + str(list_of_objects))
    #list of unique objects
    print('Unique object names in the list \n' + str(find_unique(list_of_objects)[0]))
    #number of unique objects
    print('Number of unique objects in the list: ' + str(find_unique(list_of_objects)[1]))