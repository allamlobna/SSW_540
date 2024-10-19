'''Finding unique string In a finding-all-pairs game, 
the player should find all duplicate objects and 
eliminate them. In the end, no objects are left. 
Some objects may exist as repeated pairs though. 
Therefore, each object may exist only in an even number. 
We need to play a similar game. Your code should populate 
an array with a list of object names. Object names can 
exist in pairs or non-pairs. Now your code should play the 
game of discovering any unique objects. Unique objects are 
objects that exist only once in the array. If an object 
is mentioned more than once (i.e. twice or more), it is not a unique object. '''


TEST = ['tim', 'lobna', 'mama', 'baba', 'kerry', 'mama', 'baba', 'hassan']
#['baba', 'baba', 'hassan', 'kerry', 'lobna', 'mama', 'mama', 'tim']

TEST_2 = ['E']
TEST_3 = [5, 6, 7, 4, 3, 2, 2, 1, 6]
TEST_4 = ['a', 'b', 'b', 'b', 'c','d','e']

def find_pairs(string_names: list):
    string_names.sort()
    unique_list = []
    not_unique = []
    last_val = string_names[0]
    
    if len(string_names) == 1:          #if there's only one value, it must be unique
        unique_list = string_names
        
    for i in range(1, len(string_names)):
        cur_val = string_names[i]
        if i < len(string_names)-1:    #take care of everything before the last val
            if cur_val != last_val:
                if len(unique_list)>0:
                    if last_val != unique_list[-1]:
                        if len(not_unique)>0:
                            if last_val != not_unique[-1]:
                                unique_list.append(last_val)
                            else:
                                not_unique.append(last_val)
                    else:
                        unique_list.append(last_val)  
                elif len(not_unique)>0:
                    if last_val != not_unique[-1]:
                        unique_list.append(last_val)
            else:
                not_unique.append(last_val)
            last_val = cur_val
            
        else:               #last val
            if len(unique_list)>0 and len(not_unique)>0:
                if cur_val != unique_list[-1] or cur_val != not_unique[-1]:
                    unique_list.append(cur_val)
            elif len(unique_list)>0:
                if cur_val != unique_list[-1]:
                    unique_list.append(cur_val)
            elif cur_val != not_unique[-1]:
                unique_list.append(cur_val)

            
                
    return print(unique_list)
            

if __name__ == '__main__':
    
    find_pairs(TEST_3)