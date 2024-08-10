# 2. Finding All Matches:

import re

text = "The rain in Spain" # Sample text
result = re.findall(r"\b\w+ain\b", text) # Find all words ending with
'ain'
print(result) # Print the list of matched words