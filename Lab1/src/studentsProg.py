
#Accept user ids attending pythong class , web class seperated by space
#find python students and web students the user ids using split function with space

pythonstds = input("Enter Student ids attending python class seperated by space ").split()
webstds    = input("Enter Student ids attending web class seperated by space ").split()

#Initialize 2 lists one for common studnets and another for not common students
stdcommon = list()
stdnotcommon = list()

#Iterate through Pythong userid list check if user exist in web user id list
for i in range(0, len(pythonstds)):
    if (pythonstds[i] in webstds):
        stdcommon.append(pythonstds[i]) #If python user id exist in web user ids list then add to common list
    else:
        stdnotcommon.append(pythonstds[i]) #If python user id exist in web user ids list then add to not common list

#Need to identify if any students from web user id list not in python list add to not common list
for i in range(0 , len(webstds)):
    if(webstds[i] not in pythonstds):
        stdnotcommon.append(webstds[i])


print("\nStudnets took python and web classes ", end="" )
for i in range( 0,len(stdcommon)):
      print(stdcommon[i], end =" ")

print ("\nStudents doesn't have common classes ", end = "")
for i in range( 0,len(stdnotcommon)):
      print(stdnotcommon[i], end =" ")