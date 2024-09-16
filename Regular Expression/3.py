# 3. Replacing Text:
import re

text = "The rain in Spain" # Sample text
text = re.sub(r"rain", "sunshine", text) # Replace 'rain' with 'sunshine'
print(text) # Print the modified text