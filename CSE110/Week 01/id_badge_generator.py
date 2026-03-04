print('Please enter the following information:')

firstname = input('First name:')
lastname = input('Last name:')
email = input('Email address:')
phonenumber = input('Phone number:')
jobtitle = input('ob Title:')
idnumber = input('ID Number:')

print('The ID Card is:')
print('---------------------------------------')

print(f"{lastname.uper()}, {firstname.capitalize()}")
print(f"{jobtitle.title()}")
print(f"ID: {idnumber()}")
print()
print(f"{email.lower}")
print(f"{phonenumber}")
