#Acessing the elements of string

names="Areesha,Haris"
print(names[0:5])

#Length of a string
names="Areesha,Haris"
print(len(names))

fruit="Mango"
len1=len(fruit)
print("The length of the word Mango is",len1)

#String as an array

fruit="Mango"
print(fruit[0:4]) #including 0 but not 4
print(fruit[:4])
print(fruit[1:4]) #including 1 but not 4
print(fruit[0:-3])
print(fruit[-1:-3])
print(fruit[-3:-1])

#Quick Quiz:
nm="Harry"
print(nm[-4:-2])

#Strings methods (Strings are immutable)
# i.upper() - Converts the string into upper case
string1="areesha"
print(string1.upper())

# ii.lower() - Convers the string into lower case
string1="AREESHA"
print(string1.lower())

# iii.strip() -  Removes white spaces before and after the string.
string1="    Areesha Naeem      "
print(string1.strip())

# iv.rstrip() - removes the trailing characters
string1="Hello !!!!!!"
print(string1.rstrip("!"))

#v.replaces() - replaces all occurences of a string with another string.
string1="Areesha , Ayesha , Areesha"
print(string1.replace("Areesha" , "Haris"))

#vi.split() - split the given string at he specified instance and returns the separated strings.
string1="Areesha Naeem Haris"
print(string1.split(" "))

#vii.capitalize() - turns only the first character of the string to upper case and rest to lower case
blogheading="introduction to Python"
print(blogheading.capitalize())

#viii.center() - aligns the string to the centre.
str1="Welcome to the Console!!!"
print(len(str1))
print(len(str1.center(50)))

#viii.count()
string1="Areesha Haris Areesha Khan Bangash Areesha"
print(string1.count("Areesha"))

#ix.endswith()
str1="Welcome to the console !!!"
print(str1.endswith("!!!"))

# x.find()
str1="He's name is Haris. he is an honest man"
print(str1.find("is"))

# xi.isalnum()
str1="Welcometotheconsole"
print(str1.isalnum())

# xii. isalpha()
str1="Welcome"
print(str1.isalpha())

# xiii.islower()
str="welcome to the challenge"
print(str.islower())

# xiv. isprintable()
str1="Areesha Naeem"
print(str1.isprintable())

# xv.istitle()
name="Vampire Dairies"
print(name.istitle())

# xvi.swapcases()
str2="welcome to the class"
print(str2.swapcase())



