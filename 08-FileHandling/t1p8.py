###
# Reads the entire contents of a file
#
def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

# reads the entire file and splits lines into array
file_content = read_from_file('pets.txt')
file_lines = file_content.splitlines()


words = 0

for line in file_lines:
   count = 1
   for char in line:
      if char == " ":
         count += 1
   words += count
   
print(f"There are {words} words")