#strip()
str1="!!!!! Hello !!!!!"
print(str1.strip("!o"))   #remove the "!",and " "

name="@@@$$$%%% kiran kumar ****&&&&"
print(name.strip("@,&"))

n1="kirankumar"

print(n1.strip("kr")) #remove the name first latter "k"and last latter"r" was removed remaining not removed

#lstrip()
str1="!!!!! Hello !!!!!"
print(str1.lstrip("!o"))   #we can removed left side character  only

name="@@@$$$%%% kiran kumar ****@@@@@"
print(name.lstrip("@,*"))  #    "*" is not removed because "*" is right side character so not removed


#rstrip()
str1="!!!!! Hello !!!!!"
print(str1.rstrip("!o"))   #we can removed right side character  only

name="@@@$$$%%% kiran kumar ****@@@@@"
print(name.rstrip("@,*"))  #  left side "@" character not removed

