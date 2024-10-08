'''2. Uses conditionals (if-then-else) and exception handling.
Your code should accept the (unsorted) first and last names of 9 students 
and then randomly combine sets of three students into the same group. 
Then, your code should display the three groups of students.
To make sure the student assignment is random, we apply a simple rule. 
If students' names are to be sorted based on last names, 
then any two students following each other in the 
sorted array cannot be in the same group.  '''


#Test Cases
#Randomized list of 9 first and last names - good
STUDENT_NAMES_GOOD = ['Yahya Combs', 'Zara Doyle', 'Zachery Oconnor', 'Faye Potter', 'Constance Farley', 'Umar Vasquez', 'Tiffany Bell', 'Hayley Chase', 'Aran Mcmillan']
#Randomized list of eight first and last names - bad
STUDENT_NAMES_EIGHT = ['Yahya Combs', 'Zara Doyle', 'Zachery Oconnor', 'Faye Potter', 'Constance Farley', 'Umar Vasquez', 'Tiffany Bell', 'Hayley Chase']
#Randomized list of eight first and last names and an incorrect data type - bad
STUDENT_NAMES_INT = ['Yahya Combs', 'Zara Doyle', 9, 'Faye Potter', 'Constance Farley', 'Umar Vasquez', 'Tiffany Bell', 'Hayley Chase']
#Randomized list 9 first names - bad
STUDENT_NAMES_SINGLE = ['Yahya', 'Zara', 'Zachery', 'Faye', 'Constance', 'Umar', 'Tiffany', 'Hayley', 'Aran']
#One name. Not a list - bad
STUDENT_NAMES_STRING = 'John Smith'

def sorted_names(names_list):
    '''accepts a list of 9 student first and last names.
    randomizes by sorting last names ascending
    then creates groups by arranging each sorted name into
    a group sequentially. Groups names into 3 groups of 3 
    and prints each group'''

    if not isinstance(names_list, list):
        raise TypeError('The input provided is not a list.')
    elif any(not isinstance(i, str) for i in names_list):
        raise ValueError('Must be a list of strings.')
    elif any(len(i.split()) != 2 for i in names_list):
        raise ValueError('Each student must have a first and last name.')
    elif len(names_list) != 9:
        raise ValueError('Incorrect number of students. Expected 9 names.')
    else:
        names_list.sort(key=lambda x: x.split()[1])
        group_a = []
        group_b = []
        group_c = []
        i = 0
        while i < len(names_list):
            group_a.append(names_list[i])
            i = i+1
            group_b.append(names_list[i])
            i = i+1
            group_c.append(names_list[i])
            i = i+1    
        return print('Group A: ' + str(group_a), '\nGroup B: ' + str(group_b), '\nGroup C: ' + str(group_c))

if __name__ == '__main__':
    '''Replace STUDENT_NAMES_GOOD with your list of student names'''
    sorted_names(STUDENT_NAMES_GOOD)
