

def num_check(question, low):
    
    valid = False
    while not valid:

        error = "please enter an integer that is more or equal to zero {}".format(low)
            
        
        try:
            
            response = int(input(question)) 

            if response >= low:
                return response
            

            else:
                print(error)
                print()
        
        except ValueError:
            print(error) 
            print ()
            
            
def int_bits():
    
    
    
    
    var_integer = num_check("please enter an integer: " , 0)
    
    var_binary = "{0:b}".format(var_integer)



    num_bits = len(var_binary)
    
    
    print()
    print("{} in binary is {}".format(var_integer, var_binary))
    print("# of bits is {}".format(num_bits))
    
    return ""

int_bits()