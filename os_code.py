## in this we will try to print current (DIRECTORY)folder path , (DIRECTORY)folder inside that (DIRECTORY)folder and files inside that folder


import os
##this is target location where we will find the all things i have mentioned above

#path =  "C:\Users\Vivek"

##when we copy path from file in our computer format is "C:\USers\Vivek\desktop\" backslash
##and we know that "\n" "\t" are special character for "new line" and "tab"
##so we can do three things first

##using raw string  ## in this repo you can find more information about "raw string" and "/" https://github.com/Vivekkoranga1/RegEx-re-Python-Basics-Examples 
#path = r"C:\Users\Vivek" valid
#path = "C:\\Users\\Vivek" valid because "\" is used for escape

path = "C://Users//Vivek" #valid Python uses this format



for current_location,dir_names,file_names in os.walk(path):
    print("CURRENT LOCATION :",current_location)
    print("DIRECTORIES :",dir_names)
    print("FILES :",file_names)
    print() ## for empty line 
    


