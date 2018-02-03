#define processSentence function
def processSentence(sentence ):
    print(sentence)
    words = sentence.split()
    n = len(words)

    #Iterate through words print 1 to n-1 Middle words in the sentense
    print("\nMiddle words in the sentense : ", end ="")
    for i in  range(1,n-1):
         print( words[i] , end= " ")

    #find longest word
    x = 0
    lword = 0
    #Iterate through all the words compare length and set identify index of the long word
    for i in range(0,n):
        if (lword < len(words[i])):
             lword = len(words[i])
             x = i

    print('\nLongest word : ' , words[x])

    #Iterate through all the words use print each word in reverse
    print('Sentense with reverse words : ',  end= "")
    for i in range(0,n):
        print(words[i][::-1] , end= " ")

#Accept sentese from User
senten = input("Enter sentense : ")
#call function to processSentense
processSentence(senten)
