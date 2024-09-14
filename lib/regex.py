import re


# Phone number validation (handles different formats)
phone_number = r"^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$"
phone_regex = re.compile(phone_number)


name = r"^[A-Z][a-zA-Z'-]*(?: [A-Z][a-zA-Z'-]*)*$"
name_regex = re.compile(name)

# Email validation (first character must be a letter)
email_address = r"^[a-zA-Z][a-zA-Z0-9_.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
email_regex = re.compile(email_address)
