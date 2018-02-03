pythonstds = input("Enter Student ids attending python class with space ").split()
webstds    = input("Enter Student ids attending web class with space ").split()

stdcommon = list()
stdnotcommon = list()


for i in range(0, len(pythonstds)):
    if (pythonstds[i] in webstds):
        stdcommon.append(pythonstds[i])
    else:
        stdnotcommon.append(pythonstds[i])

for i in range(0 , len(webstds)):
    if(webstds[i] not in pythonstds):
        stdnotcommon.append(webstds[i])


print("\nStudnets took python and web classes ", end="" )
for i in range( 0,len(stdcommon)):
      print(stdcommon[i], end =" ")

print ("\nStudents doesn't have common classes ", end = "")
for i in range( 0,len(stdnotcommon)):
      print(stdnotcommon[i], end =" ")