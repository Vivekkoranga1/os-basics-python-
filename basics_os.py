##here we will discuss the basics of os module 
## os moudle will help us to intearct with computer os 
## we are learning this because we can perform various task like open notepad like things from os and we will use this module for big projects later

import os 
from datetime import datetime

##It will print names of methods,fucntions,property and many more
##It is like Opening a toolbox and seeing all the tools inside
##but not knowing how each tool works
print(dir(os))


##for knowing how each tool work we can use 
print(os.system.__doc__)


##And same things also we can done with module itself how a module works
print(os.__doc__)

##LEARNING BASICS METHODS OF OS MOUDLE

##this function is use for printing current working directory 
print(os.getcwd())


##this function is use for changing the current working directory
os.chdir("<path>") ##put path inside <Path> for changing the path 


##os.listdir() this function  print the directory and files . If no argument given then current folder ,if argument given then that postion 
##print all the  files and sub folders present in current folder
print(os.listdir())

##print all the  files and sub folders present in given_path  folder using giving path argument
print(os.listdir("<path>")) ##put your path <path>

## If directory(folder),file already exist and you try to make them it will throw error
##create directory(folder)
os.mkdir("vivek_os_repo")

##create directory(folder) with multiple levels
##this is slight different from mkdir here we can create multiple level at once in mkdir we cannot create multiple level
os.makedirs("vivek/repo/os")



##delete directory(folder)
os.rmdir("vivek_os_repo")
##sometimes windows system not allow you to delete folder permission denied error can come

##delete directory(folder) at multiple levels
##this is slight different from rmdir here we can delete folders at  multiple level at once recursively delete
os.removedirs("vivek/repo/os")
##sometimes windows system not allow you to delete folder permission denied error can come

##rename directory(folder) and rename files
##renaming file 
os.rename("vive.txt","vivek.txt")
##renaming folder
os.rename("vivek","vive")


##printing information about the files
##it is easy in scripting powershell  to do this types of operation in python it is confusing 
print(os.stat("vivek.txt"))
##It print information about files
##let's try to print size
print(os.stat("vivek.txt").st_size)
##let'ss print modification time
modification_time = os.stat("vivek.txt").st_mtime ## it return a time stamp
##converting modification_time to human readable time 
print(datetime.fromtimestamp(modification_time))