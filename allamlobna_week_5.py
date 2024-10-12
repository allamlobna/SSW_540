'''String manipulation
When working on security messages, we always 
need to strip away all spaces and make all letters
capital. By that we mean, a statement like 
'The world population is increasing rapidly' 
shall be converted to 'THEWORLDPOPULATIONISINCREASINGRAPIDLY'. 
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


#Test Cases
TEST = 'The world population is increasing rapidly'
TEST_NS = 'Theworldpopulationisincreasingrapidly'

def cypher(msg: str):
    '''Cyphers the input string by removing all spaces,
    changes all characters to upper case values, and saves
    the indexes of all spaces that were removed in a list. 
    Returns a string and list.'''
    msg_list = []
    cyph_msg = []
    i_space = []
    _i = 0
    for c in msg:
        msg_list.append(c)
        
    for c in msg_list:
        if c  == ' ':
            i_space.append(_i)
        else:
            cyph_msg.append(c)
        _i += 1
        
    cyph_msg = ''.join(cyph_msg)
    cyph_msg = cyph_msg.upper()          
    
    return cyph_msg, i_space


def decypher(cyph_msg: str, i_space: list) -> str:
    '''Decyphers the input by capitalizing the first letter 
    and lowering the rest,inserts a space for every value in 
    the index list, and returns a string.'''
    split_cyph = []
    n = 0
    cyph_msg = cyph_msg.capitalize()
    
    for c in cyph_msg:
        split_cyph.append(c)
        
    for i in i_space:
        split_cyph.insert(i, ' ')
        
    split_cyph = ''.join(split_cyph)
        
    return split_cyph
    

if __name__ == '__main__':
    
    message = input('Insert message to be cyphered: ')
    cyphered_msg, cyphered_i = cypher(message)
    print('Output of cyphering function: \nCyphered message: ' + cyphered_msg, 
          '\nThe indexes of all spaces that were removed:' + str(cyphered_i))
    decypher_msg = decypher(cyphered_msg, cyphered_i)
    print('Output of decyphering function: \nDecyphered message: ' + decypher_msg)
    