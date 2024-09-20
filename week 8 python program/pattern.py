#Encoding problem - Input is a message and  a pattern. Both strings. Output is the message written in the form
#of the pattern. 
#Eg -  Message - "I Love India".
 #     Pattern - "*** **** ** **********     *****"
  #    Output  - "ILo veIn di aILoveIndi     aILov"

   #  Note how you replace each * in the pattern with the letter in the message, the space in the message doesn't
    # matter, but the space(s) in the pattern matters.
message = "I Love India"
pattern = "*** **** ** **********     *****"
pattern = pattern.strip()
message = message.replace(' ', '')
encoded_message = ''
for pattern_char in pattern:
    if pattern_char == '*':
        encoded_message += message[0]
        message = message[1:]
    else:
        encoded_message += pattern_char
print(encoded_message)