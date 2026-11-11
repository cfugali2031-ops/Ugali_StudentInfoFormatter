# Version 2: Added string formatting
# Program cleans and formats name, section, and subject using string methods.

# 1. Gather user inputs
first_name = input("Enter first name: Cameron")
last_name = input("Enter last name: Ugali")
section = input("Enter section: Anthurium
favorite_subject = input("Enter favorite subject: Health

# 2. Clean and format the strings
# Combine first and last name, remove extra spaces, and apply Title Case
full_name = f"{first_name.strip()} {last_name.strip()}".title()

# Convert full name and section to UPPERCASE
name_code = full_name.upper()
formatted_section = section.strip().upper()

# Convert favorite subject to Title Case
formatted_subject = favorite_subject.strip().title()

# Calculate the total character count of the formatted full name
char_count = len(full_name)

# 3. Display the standardized output
print("\nFormatted Output:")
print(f"Name: {full_name}")
print(f"Name Code: {name_code}")
print(f"Section: {formatted_section}")
print(f"Favorite Subject: {formatted_subject}")
print(f"Character Count: {char_count}")