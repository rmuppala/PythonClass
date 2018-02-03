
#a)	The password length should be in range 6-16 characters
#b)	Should have atleast one number
#c)	Should have atleast  one special character in [$@!*]
#d)	Should have atleast  one lowercase and atleast  one uppercase character

passwd = input("Enter password : ")

#validate password
length = len(passwd)

invalidLength = digityes = loweryes = upperyes = specialChar = False;


if (length < 6  or length > 16):
    invalidLength = True;

for i in range(0, length):
    if (passwd[i].isnumeric()): #any letter is numeric
              digityes = True;
    if(passwd[i].islower()):  # any letter is lower
              loweryes = True;
    if(passwd[i].isupper()):  # any letter is upper
            upperyes = True;
    if( passwd[i]=='$' or  passwd[i]=='@' or passwd[i]=='!' or passwd[i]=='*' ): # any letter got special char $@!*
        specialChar = True;


if (invalidLength or (digityes == False)  or (loweryes == False) or (upperyes == False) or ( specialChar == False)) :
        print("INVALID PASSWORD ")
        print("The password length should be in range 6-16 characters")
        print("Should have atleast one number")
        print("Should have atleast  one special character in [$@!*]")
        print("Should have atleast  one lowercase and atleast  one uppercase character")
else:
    print("VALID PASSWORD ENTERED")