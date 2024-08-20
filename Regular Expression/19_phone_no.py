# 2. Validate a phone number (format: XXX-XXX-XXXX):


import re # Import the re module
# phone_number = "123-456-7890" # Sample phone number

print("Number format accepted: 123-456-7890")
phone_number = input("Enter the phone No. : ") # Take input from the user


if re.match(r'^\d{3}-\d{3}-\d{4}$', phone_number): # Check if the phone number matches the pattern
    print("Valid phone number") # Print if valid
else:
    print("Invalid phone number") # Print if invalid

