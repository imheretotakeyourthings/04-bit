
# Heading



def statment_gen(text, decoration):
    
    
    ends = decoration * 5
    
    
    statment_gen = "{} {} {}".format(ends, text , ends)
    
    return""

#the number checker
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

#the instructions
def instruction():   
    
    statment_gen ("instruction / information" , "=")
    print()
    print("please choose a data type (image / text / integer)")
    print()
    print("This is a program that assumes that images are being represented in 24 bit colour (ie: 24 bits per pixel).For text, we assume that ascii encoding is being uesd (8 bits per character)")
    print()
    print("complete as many calculations as necessery, pressing <enter> at the end of each calculation or any key to quit")
    print()
    
    return ""


# caluculates the # of bits for text (# of characters x 8)
def text_bits ():
    
    
    print()
    
    var_text = input("enter some text: ")
    
    
    var_length = len(var_text)
    num_bits = 8 * var_length


    print()
    print("\'{}\' has {} characters".format(var_text, var_length))
    print("# of bits is {} x 8".format(var_length))
    print("We need {} nits to represent {}".format(num_bits, var_text))
    print()
    
    return ""

# finds # of bits for 24 bit colour
def image_bits ():
    
    
    
    image_width = num_check("Image width?: ", 1)
    image_height = num_check("Image height?: ", 1)
    
    num_pix = image_width * image_height
    
    num_bits = num_pix * 24
    
    
    print()
    print("# of pixels = {} x {} = {}".format(image_height,
                                              image_width, num_pix))
    print("# bits = {} x 24 = {}".format(num_pix, num_bits))
    print()
    
    return ""

#converts dec into bin and states how 
# many bits  are needed to represent the original integer
def int_bits():
    
    
    
    
    var_integer = num_check("please enter an integer: " , 0)
    
    var_binary = "{0:b}".format(var_integer)



    num_bits = len(var_binary)
    
    
    print()
    print("{} in binary is {}".format(var_integer, var_binary))
    print("# of bits is {}".format(num_bits))
    
    return ""


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

# ****** MAIN ROUTINE STARTS HERE ********* 


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



#shows the instructions 
first_time = input("press <enter> for instructions or any key to continue")

if first_time == "":
    instruction()



#heading
statment_gen("bit calcultor for Integers, Text & Image", "-")


#the loop thing?
keep_going = ""
while keep_going == "":           
    data_type = user_choice()
    print("your choice is: ", data_type)
    print()
    if data_type == "integer":
        int_bits()
    
    
    elif data_type == "image":
        image_bits()
    
    
    else:
     text_bits()
     
     
    print()
    keep_going = input("press <enter> to continue or any key to quit")

