def statement_generator(text, decoration):
    
    ends = decoration * 6
    
    statement = " {} {} {} ".format(ends, text, ends)
    
    print()
    print(statement)
    print()



statement_generator("bit calcultor for Integers, Text & Images")
