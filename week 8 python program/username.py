#Check if the username and password is correct. 
 #    Username should contain the char @  and '.com' or '.edu' or '.tech' or 'org' at the end.
  #   passward is the first, third, and last 3 letters of the username followed by the first three letters of the 
   #  name of the company mentioned in the username, followed by any 3 numbers.
    # eg username : myname@sayur.com. password - mnamesay123 

username = input('Enter your username: ')
if not (username.endswith('.com') or username.endswith('.edu') or username.endswith('.tech') or username.endswith('.org')):
    print('Invalid username')
else:
    company_name = username.split('@')[1].split('.')[0]
    expected_password = username[0] + username[2] + username[3] + company_name[:3] + '123'
    print("password:",expected_password)
