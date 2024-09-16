# 1. Searching for a Pattern:

import re # Import the re module to work with regular expressions

text = "The rain in Spain" # Sample text
result = re.search(r"\bS\w+", text) # Search for words starting with "S"
if result:
    print(result.group()) # Print the matched word if found