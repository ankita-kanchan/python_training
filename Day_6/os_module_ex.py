import os

#get current directory

print(os.getcwd())

#changing directory

os.chdir('C:\\Users\\ankit\\Desktop\\Python Training')

print(os.getcwd())

#list of directories and files

print(os.listdir()) #cwd
print(os.listdir("C:\\"))

Making a new dir
os.mkdir("Day7")
print(os.listdir())

renaming dir or file
os.rename("Day7","Demo")
print(os.listdir())

#removing dir
os.remove("Demo.py") #remove file
print(os.listdir())
os.rmdir("Demo") #remove Dir
print(os.listdir())


