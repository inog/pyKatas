""" Play around with files
"""

f = open("demo.txt", "w")  # creating and writing a new file
f.write("I just created this file.")
f.close()


f = open("demo.txt", "r")  # read
print(f.read())
