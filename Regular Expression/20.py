# Phone number checking different formate

import re

def validate_phone_number():
    print("Number format accepted: 123-456-7890")
    phone_number = input("Enter the phone number: ")

    pattern = r'^\d{3}-\d{3}-\d{4}$'
    if re.match(pattern, phone_number):
        print("Valid phone number")
    else:
        print("Invalid phone number")

validate_phone_number()
