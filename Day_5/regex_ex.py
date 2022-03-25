import re
pattern ="^P....n$" #P and 
output=re.match(pattern,"Pjdnvkfd")
if(output):
    print("Match")
else:
    print("No Match")

#[] - square brackets
#specifies the set of characters that you want to match
import re
pattern="[x-z]"  # x,y or z
#[x-y] => [xyz]
#[1-4] =>[1234]
res=re.match(pattern,"xa")
if(res):
    print("Matched")
else:
    print("No Match")

# . - Period
#matches any single character (except newline '\n')


#Meta Characters

# [] . ^ $ + * ? {} \ |

# . - Period
#matches any single character (except newline '\n')


# ^ caret Symbol
#used to check if string starts with certain character

#$ Doller Symbol
#used to check if string ends with certain character

#* - Star Symbol
# matches zero or more occurences of pattern
#ma*n  => man(yes) maaan(yes) main(no) woman(yes) mn(yes)

#+ plus
#one or more occurences of pattern
#ma+n => man(yes) maaan(yes) main( no -a is not followed by n)

#? -> Question mark
#ma?n -> mn(no) ma(no) man(yes) maaan(no)  main(no) woman(yes)

#{} =>
{n,m} at least n and at most m repitions of the pattern are left

##a{2,3}
##abc dat -> not match
##
##abc daat -> match(daat)
##
##aabc daaat -> 2 match aabc daaat

##[0-9]{2,4} # atleast 2 digit but not more than 4 
##
##ab123ndgn -> match
##
##12

# | - Alteration
# veritacal bar used for alteration (or operand)
#a|b
#cbs(yes)
#ajk(yes)
#juk(no)
#abcde(yes)


#() - group
##(a|b|c)xy
##
##abc xz(no)
##
##abxy(yes)
##
##axy bcxy (yes)

# \ - Backslash
# used for escaping characters including meta characters
#\$a => $ will be treated as just a symbol not special character

#\athe => the car(yes)
#in the car (no) 

#Special Sequences

#\b -> matches if specific char is at begining or end of word

#\bfoo -> starts with foo
#food(yes)
#football(yes)

#foo\b -> ends with foo
#afoo(yes)

#\B => matches if specific char are not at begining or end of word
#\Bfoo -> not starting with foo
#football(no)
#afoo(yes)

#\d -> match digit
#800hhd (3 matches)
#abcd(no)

#\D -> non digit [^0-9]

#\s -> matches white spaces [\t\n\r\f\v]
#\S -> non white spaces [^ \t\n\r\f\v]

#\w => alphanumberic characters [a-zA-Z0-9_]
#W => non alphanumberic characters [^ a-zA-Z0-9_]

#\Z => specific characters are at the end of the string



import re

#re.findall()
#list of strings containing all matches

st="Hello 45 this is 89"
pattern="\d+"

res= re.findall(pattern,st)
print(res)


#re.split()
#splits the string where pattern is matched
st="Hello 45 this is 89"# hello, this is ,""
pattern="\d+" #
res= re.split(pattern,st,1)
print(res)

#re.sub()
#re.sub(patten,replace,string)
#program for removing white spaces
st="Hello 45 this is 89"
pattern="\s+"
res= re.sub(pattern,'',st)
print(res)


#subn
#returns the tuple(new string,no of replacements)
st="Hello 45 this is 89"
pattern="\s+"
res= re.subn(pattern,'',st)
print(res)


#re.search()
#search for the first location of the pattern
#match =re.seach(pattern,str)
st="i like football"
pattern="[foo]"
res= re.search(pattern,st)
print(res.group(0))


#Match Objects

#group()

import re

pattern="(\w+)"

st="My name is Ankita"

op= re.match(pattern,st)
print(op.group(0))

print(op.start()) # start index
print(op.end()) #end index
print(op.span()) # tuple of start and end index
print(op.string) # string of match

#url regex =>(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))\

# mobile no,
# \d{10}
# \d{3}\d{3}\d{4}

#email id

#name@domain.com

#regex => ([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9]+(\.[A-Z|a-z]{2,})+

#Password Regex
#1.uppercase
#2.lowercase
#3.digits
#4.any special char @#$%^&+=

#regex=>[A-Za-z0-9@#$%^&+_]{8,}

#vehicle no :
#regex => [A-Z]{2}[ -][0-9]{2}[ -][A-Z]{2}[ -][0-9]{4}$
#vehicle no. =>^[A-Z]{2}[ -][0-9]{1,2}(?: [A-Z])?(?: [A-Z]*)? [0-9]{4}$







