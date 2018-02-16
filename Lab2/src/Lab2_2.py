def modifyContact(contList, name, phno):
    for cont in contList:
        if(cont["name"] == name):
            cont["number"] = phno

def main():
    cont='Y'
    contList = list()

    while cont == 'Y':   #Read user details
        contDetl = dict() #each user details
        name = input("Enter username  " )
        phno = input("Enter contat number : " )
        if(len(phno) != 10): #exit if phone number is not 10 digits
            print("Phone number should be 10 digit")
            exit()
        email = input("Enter email id")
        contDetl["name"] = name
        contDetl["number"] = phno
        contDetl["email"] = email
        contList.append(contDetl) #create users list
        cont = input("Do you want to continue 'Y/N' ")


    contName = input("Enter contact name to modify contact number")
    newph = input("Enter new contact number for " + contName)

    print("Users details : " , contList)
    modifyContact(contList, contName, newph)
    print("New user details after modifying phone number : " , contList)

if __name__ == "__main__":
    main()