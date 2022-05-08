
# ****** MAIN ROUTINE STARTS HERE *********

def statement_generator(text, decoration):
    
    ends = decoration * 6
    
    statement = " {} {} {} ".format(ends, text, ends)
    
    print()
    print(statement)
    print()


def user_choice():
    
    text_ok = ["text", "t", "txt"] 
    integer_ok = ["integer", "int", "#", "number"]
    image_ok = ["image", "picture", "pic", "img", "pix", "p"]
    vilad = False
    while not vilad:
        
        response = input("file type (integer / text / image): ").lower()    
        
        if response in text_ok:
             return "text"
         
        elif response in integer_ok:
            return "integer"
        
        elif response in image_ok:
            return  "image"
         
        elif response == "i":
            want_int = input ("press <enter> for -integer- or any keey for -image-")
            if want_int == "":
                return "integer"
            else:
                return "image"
        
        else:
            print("Please choose a valid file type!")
            print()


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



statement_generator("bit calcultor for Integers, Text & Images")

          
keep_going = ""
while keep_going == "":           
    data_type = user_choice()
    print("your choice is: ", data_type)
    print()
    if data_type == "integer":
        var_integer = num_check("enter an integer: ", 0)
    
    
    elif data_type == "image":
        image_width = num_check("Image width: ", 1)
        print()
        image_height = num_check("Image height: ", 1)
        print()
    
    
    else:
        var_text = input("enter some text: ")

