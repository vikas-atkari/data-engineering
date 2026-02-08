import re

# Example string
text = "The rain in Spain stays mainly in the plain."

# 1. Search for a pattern
pattern = r'\b\w+ain\b'  # Words ending with 'ain'
matches = re.findall(pattern, text)
print(f"Words ending with 'ain': {matches}")    

# 2. Replace a pattern
replaced_text = re.sub(r'\b\w+ain\b', 'XXX', text)
print(f"Text after replacement: {replaced_text}")

# 3. Split a string based on a pattern
split_text = re.split(r'\s+', text)
print(f"Split text: {split_text}")

# 4. Check if a pattern exists in the string
if re.search(r'\bSpain\b', text):
    print("The word 'Spain' is found in the text.")
else:    print("The word 'Spain' is not found in the text.")    

# 5. Extract all words starting with 's'
s_words = re.findall(r'\bs\w*', text)
print(f"Words starting with 's': {s_words}")    


S1 = "The BodyGuard is the best album of all time."

# Define a regex pattern to search for 'Guard'
pattern = r'\b\w+Guard\b'
# Search for the pattern in the string
match = re.search(pattern, S1)
if match:
    print(f"Found '{match.group()}' in the string.")
else:    print("Pattern not found in the string.")

S2 = "My mobile number is 123-456-7890. you can call me anytime and my email is xyz@yahoo.in"

# Define a regex pattern to search for a phone number
pattern = r'\d{3}-\d{3}-\d{4}'
# Search for the pattern in the string
match = re.search(pattern, S2)
if match:
    print(f"Found phone number: {match.group()}")
else:    print("Phone number not found in the string.")

# Define a regex pattern to search for non word characters
pattern = r'\W'
# Find all non word characters in the string
non_word_characters = re.findall(pattern, S2)
print(f"Non word characters in the string: {non_word_characters}")

S3 = "The BodyGuard is the best album of 'Whitney Houston'."

# Define a regex pattern to search for text within single quotes
pattern = r"'(.*?)'"

replacement = 'legendary musician' 
# Replace the text within single quotes with the replacement string
replaced_S3 = re.sub(pattern, replacement, S3, flags=re.IGNORECASE)
print(f"String after replacement: {replaced_S3}")   


# Format strings in Python
name = "Michael Jackson"
age = 50    
formatted_string = f"{name} is {age} years old."
print(formatted_string) 

# str.format() method
formatted_string = "{} is {} years old.".format(name, age)
print(formatted_string)

# % formatting
formatted_string = "%s is %d years old." % (name, age)
print(formatted_string)

# string is immutable in Python
s = "Hello, World!"
# s[0] = 'h'  # This will raise an error because strings are immutable  
    