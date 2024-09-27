'''Using user-defined functions. Your code should accept 
the (unsorted) first and last names of 9 students along with 
the number of courses they are studying in the current term. 
Your program should make a call to functions called "fullTime(student s)". 
The "fullTime()" function returns TRUE if the student is 
studying three courses or more and returns FALSE otherwise. 
Your program should display each student name followed 
by the word "Full-time" or "Part-time" based on the 
number of courses the student is taking.'''

#list of 9 unsorted students and the number of classes they are attending
STUDENT_NAMES_CLASSES = [('Yahya Combs', 3), ('Zara Doyle', 2), ('Zachery Oconnor', 4), ('Faye Potter', 5), 
                        ('Constance Farley', 1), ('Umar Vasquez', 6), ('Tiffany Bell', 1), 
                        ('Hayley Chase', 2), ('Aran Mcmillan',3)]

def fullTime(student):
    '''
    Args:
        student (tuple): Student Name, Number of classes.

    Returns:
        bool: false if Number of classes is less than 3,
                true if Number of classes is 3 or more
    '''
    if student[1] < 3:
        return False
    else:
        return True


if __name__ == '__main__':
    list_students = STUDENT_NAMES_CLASSES
    
    #go through list of student names and print their name and enrollment status
    for s in list_students:
        if fullTime(s) is False:
            print(s[0] + ' Part-time')
        else:
            print(s[0] + ' Full-time')