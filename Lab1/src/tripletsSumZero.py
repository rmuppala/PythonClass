try:

    intnums = list()
    triple0 = list()

    print ("Enter  numbers  separated by a single space only" )

    allnums = input().split() #split numbers seperated by space
    if(len(allnums) < 3):  print("Need atleast 3 numbers") #need min 3 numbers

    for i in allnums:
        intnums.append(int(i)) #convert data entered from input stream to int
    n = len(allnums)
    #loop through numbers to find triplet sum to zero
    for  i in range(0,n):
        fno = intnums[i]
        for j in range(i+1,n):
            sno = intnums[j]
            for k in range(j + 1, n):
               tno = intnums[k]
               sum = fno+sno+tno
               if sum == 0:
                   #print('triples %d , %d, %d sum to zero ' % (fno,sno,tno))
                   triple0.append((fno,sno,tno))

    print("Numbers you have entered : " , intnums)
    print("Triplets sum to zero " , triple0)

except ValueError: #Exception handling when converting string to int error occurs if number not intered
      print("Please enter only numbers ")

