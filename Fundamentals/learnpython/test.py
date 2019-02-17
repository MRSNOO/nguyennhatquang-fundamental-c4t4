from sys import argv
from os.path import exists
# script, first, second, third = argv
# print("\nJan\nFeb")

# print("How old are you?",end = ' ')
# age = input()
# print("What is your height?",end = ' ')
# height = input()
# print("so you are {0} years old and {1}".format(age,height))
# print("The script is called:", script)
# print("Your first variable is:", first)
# print("Your second variable is:", second)
# print("Your third variable is:", third)

# script, user_name = argv
# prompt = "> "

# print("Hi {0}, I am the {1} script".format(user_name, script))
# print("Do you like me {0}?".format(user_name))
# likes = input(prompt)

script, from_file, to_file = argv 

print("Copy from {0} to {1}".format(from_file, to_file))
intext = open(from_file)
text1 = intext.read()
print("{0} is {1} data long".format(from_file,len(text1)))
outtext = open(to_file, "w")
outtext.write(text1)

intext.close()
outtext.close()



# print("Here's your file {0}".format(filename))
# print(txt.read())
# target = open(filename)
# khi dùng các lệnh open + read lưu ý : target.close(), target.read(), target.readline()(doc 1 dong), target.truncate(xóa), target.write("stuff"), seek(0)(move chỗ đang read/write lên đầu)

 
