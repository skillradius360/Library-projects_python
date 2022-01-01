import time as t
name = []  # global var


class library():

    def __init__(self, bookslist, libraryname):
        self.bookslist = bookslist
        self.libraryname = libraryname
        self.lended_books = []
        self.named = name
        self.numbooks = {}
        self.booklist2 = list(self.bookslist)

    def book_available(self):

        no = -1 #for showing real indexes of books
        print('These are the books available :-) ')
        for books in self.booklist2:
            no += 1

            print(f'Book no {no} :{books}')

    def lend_book(self):
        try:
            for nums, books in enumerate(self.booklist2):
                self.numbooks[nums] = books
            lendinp = int(input('the book you want to lend :'))
            x = (self.numbooks[lendinp])

            self.named.append(name)
            for every_book in self.numbooks.values():
                if x in every_book:
                    t.sleep(2)
                    print('Your order is to be processed')
                    self.booklist2.remove(x)
                    t.sleep(2)
                    print('Your order is processed!Thank you for using this library')
                    t.sleep(2)
                    self.lended_books.append(f'{self.named[0]} has : {x}')
                    print(self.lended_books)
        except KeyError:
            print('This book number or varient does not exist')
            t.sleep(2)
            self.book_available()

    def add_book(self):
        add_inp = str(input('What book do you want to donate!--> ').capitalize())
        self.booklist2.append(add_inp)
        t.sleep(1)
        print('.')
        t.sleep(1)
        print('.')
        t.sleep(1)
        return 'Thank You for your kind donation :)'

 # Button
def initiate():
    condition = True
    man1 = library(['Absalom, Absalom!', 'A Time to Kill by John Grisha',
                   'The House of Mirth by Edith Wharton', 'East of Eden by John Steinbeck. '], 'raj')  # add class vars here
    print(f'Welcome to  {man1.libraryname} s Library ')

    while condition:
        playername = str(input('Your name please-->'))
        name.append(playername)
        
        user_input = eval(input('(1):Available Books\n'
                                '(2):Add Book\n'
                                '(3):Lend Book\n'
                                '(4):Exit\n'
                                ))
        if user_input == 1:
            print(man1.book_available())
        elif user_input == 2:
            print(man1.add_book())
        elif user_input == 3:
            print(man1.lend_book())
        elif user_input == 4:
            t.sleep(1)
            print('Hope to see you back soon...Cheerio!!:)')
            condition = False
        else:
            print('there is some error\n')
            initiate()


initiate()
