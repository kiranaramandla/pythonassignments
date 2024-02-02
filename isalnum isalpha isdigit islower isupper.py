#isalnum:
name="kiran42"
print(name.isalnum()) #true  #method returns True if all the characters are alphanumeric, 
                                #meaning alphabet letter (a-z) and numbers (0-9).

name="kiran4@@$2"
print(name.isalnum()) #false
name="kiran 42"
print(name.isalnum()) #false

#isalpha:
name="kiran"
print(name.isalpha()) #true    #method returns True if all the characters are alphabet letters (a-z).

name="kiran4@@$2"
print(name.isalpha()) #false
name="kiran 42"
print(name.isalpha()) #false


#isdigit:

name=" 90"
print(name.isdigit()) #false    #method returns True if all the characters are digits, otherwise False.
                                  
name="42"
print(name.isdigit()) #true
name="42 "
print(name.isdigit()) #false

#islower:

name="kiranKUMAR"
print(name.islower())  #false  #method returns True if all the characters are in lower case, otherwise False.
                                 #Numbers, symbols and spaces are not checked, only alphabet characters.
name="kirankumar"  #true
print(name.islower()) 

#isupper:

name="KIRANKUMAR"
print(name.islower())  #false  # method returns True if all the characters are in upper case, otherwise False.
                                  #Numbers, symbols and spaces are not checked, only alphabet characters.
name="kirankumar"  #true
print(name.islower())

#isspace:
name=" "
print(name.isspace())  #true  #  method returns True if all the characters in a string are whitespaces, otherwise False.
                               
name="kirankumar"  #false  
print(name.isspace())

#istitle:

name="kirankumar"
print(name.istitle())  #false    # method returns True if all words in a text start with a upper case letter, 
                                        # AND the rest of the word are lower case letters, otherwise False.
                                            # Symbols and numbers are ignored.
name="Kiranumar"
print(name.istitle()) #true







