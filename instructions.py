def statment_gen(text, decoration):
    
    
    ends = decoration * 5
    
    
    statment_gen = "{} {} {}".format(ends, text , ends)
    
    return""

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



instruction()