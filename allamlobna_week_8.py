'''Handling text file
A small grocery chain has a system that scans customers' 
personal checks and converts the amounts on the check to 
a text file. The formats of the text file are as follows:
29.35  only twenty-nine dollars and thirty-five cents
50.01  only fifty dollars and one cent
You are contracted by the grocery chain to validate that 
the textual description of each number matches the numerical 
value on the same line. You are lucky because the grocery 
chain does not accept any checks of a value higher than $100. 
You need to create the text file using any text 
editor and use it to test your code.'''


NUMBERS = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90
    }

def parser(line):
    line = line.split()
    comp_num = 0       
    num = float(line[0])
    cents = line[5].split('-')
    
    #check to see if the textual description is in the correct format
    if len(line) != 7:
        return 'Invalid Entry'

    #special case for high range
    if line[2] == 'one-hundred':
        comp_num = 100
    else:
        dollars = line[2].split('-')
        for _d in dollars:
            if _d in NUMBERS:
                comp_num = comp_num + NUMBERS.get(_d)
    
    for _c in cents:
        if _c in NUMBERS:
            comp_num = comp_num + (NUMBERS.get(_c)/100)
    
    #verification        
    if comp_num == num:
        return True
    else:
        return False
    

if __name__ == '__main__':
    #try and if less than number of values required, produce msg
    f = open("week_8_grocery.txt", "r")
    for x in f:
        print(parser(x))
    