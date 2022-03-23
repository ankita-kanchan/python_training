#String

st="Python"

print(st)

#Access the string

#indexing
print(st[0])
#negative indexing
print(st[-1])
#slicing
print(st[::-1])

# Python string operators

#plus
print("hello"+"world")
#multi
print("Hello"*3)

#iterating string
for i in "Hello":
    print(i)

#membership op with string 
print("H" in "Hello")


#format()
print("my name is {} and my age is {}".format("Jae",24))
print("my name is {name} and my age is {age}".format(name="Jae",age=24))
print("my name is {0} and my age is {1}".format("Jae",24))

#String Buit in methods

#format()
print("my name is {} and my age is {}".format("Jae",24))
print("my name is {name} and my age is {age}".format(name="Jae",age=24))
print("my name is {0} and my age is {1}".format("Jae",24))

#Formating numerical values

print("price is {:.4f}".format(3.555555555))


#lower
st="Hello"
print("Hello".lower())

#upper
print("".upper())

#capitalize()
print("hello world".capitalize())

#count()
print(st.count("l"))

#endswith()
print("have a nice day".endswith("day"))

#find
print("have a nice day".find("day"))

#strip
#removes leading and trailing spaces
print("  Hi  ".strip())

#replace
print("Demo".replace("o","e"))

#split()
print("hello@world".split("@"))

#reverse the string
print("".join(reversed("demo")))


