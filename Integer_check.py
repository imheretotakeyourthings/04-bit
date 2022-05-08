# checks input is a number more then zero
from email.mime import image


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





keep_going = ""
while keep_going == "":           
    print()
    var_integer = num_check("enter an integer: ", 0)
    print()
    
    image_width = num_check("Image width: ", 1)
    print()
    image_height = num_check("Image height: ", 1)
    print()
