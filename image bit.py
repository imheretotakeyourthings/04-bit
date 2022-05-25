

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


image_bits()














