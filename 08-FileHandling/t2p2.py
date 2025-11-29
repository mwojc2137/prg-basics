###
# Writes Seven Wonders of the World to a file
#
seven_wonders = [
   "Great Wall of China",
   "Petra",
   "Christ the Redeemer",
   "Machu Picchu",
   "Chichen Itza",
   "Roman Colosseum",
   "Taj Mahal"
]

# Name of the file to write to
file_name = 'seven_wonders.txt'

# Sort data alphabetically
seven_wonders.sort()

# Write data to the file
with open(file_name, 'w') as file:
      count = 1
      for item in seven_wonders:
        file.write(f"{count}. {item}\n")
        count += 1