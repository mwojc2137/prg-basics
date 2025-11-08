###
# Counts vowels in the text
#
text = "Yet another sample text"
vowels = "aeiouAEIOU"
vowel_count = 0
char_no = 0

# Count vowels in the text
while char_no < len(text):
    if text[char_no] in vowels:
        vowel_count += 1
    char_no += 1

print(f"The number of vowels in the text is: {vowel_count}")
