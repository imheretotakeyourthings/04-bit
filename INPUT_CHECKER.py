


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
            
            
keep_going = ""
while keep_going == "":           
    data_type = user_choice()
    print("your choice is: ", data_type)

    print()

         