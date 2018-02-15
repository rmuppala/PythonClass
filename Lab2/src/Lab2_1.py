
def bookscanbuy( books , minRange, maxRange):
    bookslist = []
    print("Books Details " , books)
    for bookname in books.keys() :
        bookvalue = books[bookname]
        if ( bookvalue >= minRange and bookvalue <=  maxRange):
          bookslist.append(bookname)
    return bookslist


def main():
    cont='Y'
    books = dict()
    while cont == 'Y':   #Continue read book until user say 'N'
        book = input("Enter book name  " )
        price = input("Enter price : " )
        books[book] = price  #Create books dictionary
        cont = input("Do you want to continue 'Y/N' ")
    min = input("What is the minimum price you can a buy a book ")
    max = input("What is the maximum price you can a buy a book ")
    blist = bookscanbuy(books, min,max)
    print("Books can buy in range " ,  min, " " , max , " ", blist)

if __name__ == "__main__":
    main()