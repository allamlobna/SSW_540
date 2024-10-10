'''String manipulation
When working on security messages, we always 
need to strip away all spaces and make all letters
capital. By that we mean, a statement like 
"The world population is increasing rapidly" 
shall be converted to "THEWORLDPOPULATIONISINCREASINGRAPIDLY". 
Hence, the cyphering function shall remove all 
spaces and convert all letters to capital letters, 
and also return the cyphered text and an array of 
the exact points in the text where spaces used to be. 
The deciphering function must insert the spaces back 
at the correct points and convert all letters to 
small letters except the first letter in the statement. 
For simplicity, we ignore all punctuations and special 
characters, and assume the maximum number of letters 
in a message is 140 letters. '''


TEST = "The world population is increasing rapidly"
TEST_NS = "Theworldpopulationisincreasingrapidly"

def cypher(msg):
    split_char = []
    i_space = []
    for c in msg:
        split_char.append(c)
        
    for c in split_char:
        if c  == ' ':
            try:
                i_space.append(c)
            
            except:
                print("Looks like the message didn't have any spaces!")
                
        
    
    return print(split_char), print(i_space)

if __name__ == '__main__':
    
    #message = input('Insert message to be cyphered')
    message = TEST
    cypher(message)