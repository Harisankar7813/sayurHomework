#Print the level of the password security and if the password is acceptable
 #   Weak - only alphabets or only numbers or only special chars
  #  Ok - at least one alphabet, one number and one special char
   # strong - at least three alphabets, two numbers and one special char
    #Very strong - same as strong, but at least 16 count

   # All passwords must be at least 8 chars long. You can use RegEx if you want 
password = input("Enter your password: ")
if len(password) >= 8:
    print("Password is accepted")
    #week
    if password.isalpha() or password.isdigit() or password.isalnum():
        if password.isalpha()>=3 and password.isdigit()>=2 and password.isalnum()>=1:
            if len(password) >= 16:
                print("The given password is Very strong")
            else:
                print("The given password is strong")
        else:
           print("The given password is OK")
    else:
        print("Weak")
        print("Password must contain at least one alphabet, one number and one special character.")
else:
    print("password must contain atleast 8 characters")

