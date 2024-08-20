# 1. Find all email addresses in a text:


import re # Import the re module
text = "Please contact us at support@example.com or sales@example.com"
# Sample text
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text) # Find all email addresses
print(emails) # Print the list of email addresses
