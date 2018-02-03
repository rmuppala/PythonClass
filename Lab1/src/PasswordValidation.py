#a)	The password length should be in range 6-16 characters
#b)	Should have atleast one number
#c)	Should have atleast  one special character in [$@!*]
#d)	Should have atleast  one lowercase and atleast  one uppercase character

passwd = input("Enter password : ") #take password from user

#validate password
length = len(passwd) # get length of password
invalidLength = digityes = loweryes = upperyes = specialChar = False; #set all the boolean varabiles to false


if (length < 6  or length > 16): #check length if length invalid set invalidLength true
    invalidLength = True;

for i in range(0, length):
    if (passwd[i].isnumeric()): #check if cahr is numeric, set digityes to True
              digityes = True;
    if(passwd[i].islower()):  # check if char is lower, set loweryes to True
              loweryes = True;
    if(passwd[i].isupper()):  # check if char is upper, set upperyes to True
            upperyes = True;
    # if  any char  is special char $@!* , set specialChar  to True
    if( passwd[i]=='$' or  passwd[i]=='@' or passwd[i]=='!' or passwd[i]=='*' ):
        specialChar = True;

#if any one bollean value is False then print password is invalid
if (invalidLength or (digityes == False)  or (loweryes == False) or (upperyes == False) or ( specialChar == False)) :
        print("INVALID PASSWORD ")
        print("The password length should be in range 6-16 characters")
        print("Should have atleast one number")
        print("Should have atleast  one special character in [$@!*]")
        print("Should have atleast  one lowercase and atleast  one uppercase character")
else:
    print("VALID PASSWORD ENTERED")