'''Guessing a number using loops and a function
Your code should guess a number between 0 and 50. 
The game starts by the computer requesting the user 
to generate a secret number. Then the computer guesses 
the number, but if the guess is incorrect, the computer 
asks the user if his secret number is higher or lower 
than the computer's guess. By repeating this process 
the computer will eventually pick the right number. 
The computer should keep going until the secret number 
is guessed. But is there a chance the computer is unable to make the right guess?'''
import random


def guess_random_num(x_boundary, y_boundary):
    '''Get random integer within a provided range.'''
    comp_guess = random.randint(x_boundary, y_boundary)
    return comp_guess


if __name__ == '__main__':
    '''User chooses int between 0 and 50. Script will randomly guess the
    int. User will tell the script if their value is higher or lower than
    each guess. The random int generator will base the range off of the
    user replies.'''

    while True:
        sec_number = input('Input a number between 0 and 50:')
        try:
            sec_number = int(sec_number)
        except:
            print('Must be an integer.')
            continue
        if 0 < sec_number < 50:
            y_boundary = 49 #max boundary
            x_boundary = 1 #min boundary
            rand_num = guess_random_num(x_boundary, y_boundary)
            while rand_num != sec_number:
                user_resp = input('The computer incorrectly guessed that your number is ' + 
                                  str(rand_num) + '. Is your number higher or lower? Insert H/L: ')
                
                if user_resp != 'H' and user_resp != 'L':
                    print('Response must be H or L. Please enter a valid response.')
                #check if H or L response is accurate
                elif (rand_num < sec_number and user_resp == 'H') or (rand_num > sec_number and user_resp == 'L'):
                    if user_resp == 'H':
                        x_boundary = rand_num+1
                    elif user_resp == 'L':
                        y_boundary = rand_num-1                    
                    rand_num = guess_random_num(x_boundary, y_boundary)
                else:
                    print('Are you sure? That does not seem correct.')
                    
            print('The computer guessed the correct value! It is ' + str(rand_num))
        else:
            print('Number must be between 0 and 50.')