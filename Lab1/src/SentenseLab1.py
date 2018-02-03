def processSentence(sentence ):
    print(sentence)
    words = sentence.split()
    n = len(words)

    #print middle words
    print("\nMiddle words in the sentense : ", end ="")
    for i in  range(1,n-1):
         print( words[i] , end= " ")

    #find longest word
    x = 0
    lword = 0
    for i in range(0,n):
        if (lword < len(words[i])):
             lword = len(words[i])
             x = i

    print('\nLongest word : ' , words[x])

    #print words in reverse order
    print('Sentense with reverse words : ',  end= "")
    for i in range(0,n):
        print(words[i][::-1] , end= " ")

senten = input("Enter sentense : ")
processSentence(senten)
