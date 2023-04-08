"""Hyungna Lim 3/4/2023 This program stores author and book list as key-value pairs
and allows users to view/add/del/edit values once they command.
The program can handle multiple books for each author as long as they have different title.
Every input uses capitalization strategy."""

# intro message
print('Welcome to the reading list program!\n'
      'Please enter command from the menu below.\n')


def main():
    try:
        readings = {'Sally Rooney': ['Normal People'],  # set dictionary with key(author)-value(list of book) pair
                    'Han Kang': ['Vegetarian'],
                    'J. K. Rowling': ['Harry Potter 1', 'Harry Potter 2']}
        display_menu()
        while True:     # set in a loop until getting right command input
            command = input('Command: ').lower()
            if command == 'view':
                view(readings)
            elif command == 'all':
                view_all(readings)
            elif command == 'add':
                add(readings)
            elif command == 'del':
                delete(readings)
            elif command == 'edit':
                edit(readings)
            elif command == 'exit':
                print('Thanks for using our program. Good bye!')
                break
            else:
                print('Not a valid command. Please try again!\n')
    except KeyError:    # exception handling
        print('Key error ')


def display_menu():
    print('COMMAND MENU')
    print('all - view all readings')
    print('view - View readings')
    print('add - Add a reading')
    print('edit - Edit a reading')
    print('del - Delete a reading')
    print('exit - Exit program')
    print()


def view_all(readings):
    all_readings = []   # set an empty list to get all readings
    for author in readings:     # set a loop to get key(author)-value(book) pair
        books = readings[author]    # define the list of book which is a value pair of each author key
        for book in books:      # set a loop to get multiple books from the list
            all_readings.append((author, book))     # add each author-book pair to the list
    all_readings.sort()
    print('{:<20}{:<25}'.format('AUTHOR NAME', 'BOOK TITLE'))
    for author, book in all_readings:   # set a loop to print each book in a table format
        print(f'{author:<20}{book:<25}')
    print()


def view(readings):
    author = no_blank(input('Enter the author\'s name: ').title())
    if author in readings:  # check if there is the author name in the dictionary
        books = readings[author]    # define the list of book which is a value pair of each author key
        print(f'Book(s) by {author}:')
        print(*books, sep='\n', end='\n\n')    # print the list of book without brackets & separate with new line
    else:
        print(f'There is no book by "{author}" in the list.\n')


def add(readings):
    author = no_blank(input('Enter a new author name: ').title())
    if author in readings:  # check if there is the author name in the dictionary
        books = readings[author]    # define the list of book which is a value pair of each author key
        book_to_add = no_blank(input(f'Enter the title of a new book by {author}: ').title())   # define the book to add
        if book_to_add not in books:    # check if book_to_add is not in the list
            readings[author].append(book_to_add)    # if true, add the book in the list
            print(f'The book "{book_to_add}" by {author} was added.\n')
        else:
            print(f'The book "{book_to_add}" by {author} is already in the list.\n')
    else:
        book_to_add = no_blank(input(f'Enter the book title: ').title())
        readings[author] = []   # make a new empty book list for author
        readings[author].append(book_to_add)    # add the book in the list
        print(f'The book "{book_to_add}" by {author} was added.\n')


def edit(readings):
    author = no_blank(input('Enter an author name to edit: ').title())

    if author in readings:
        books = readings[author]    # define the list of book which is a value pair of each author key

        if len(books) == 1:     # check if there is only 1 book in the list
            new_title = no_blank(input(f'Enter a new title for book "{books[0]}": ').title())   # ask new title & define
            print(f'The book "{books[0]}" was edited to "{new_title}".\n')
            books[0] = new_title    # change the value of the first(and only) book in the list
            
        elif len(books) > 1:    # check if there are multiple books in the list
            print(f'Book(s) by {author}:')
            print(*books, sep='\n')     # print the list of book without brackets & separate with new line
            book_to_edit = no_blank(input(f'Enter the book title you want to edit: ').title())  # ask which book to edit
            if book_to_edit not in books:
                print(f'There is no book titled "{book_to_edit}" in the list. Try again!\n')
            else:
                new_title = no_blank(input(f'Enter a new title to edit: ').title())  # ask new title & define
                books[books.index(book_to_edit)] = new_title    # find the index of book_to_edit and change the value
                print(f'The book "{book_to_edit}" was edited to "{new_title}".\n')
    else:
        print(f'There is no book by "{author}" in the list.\n')


def delete(readings):
    author = no_blank(input('Enter an author name to delete: ').title())
    if author in readings:
        books = readings[author]    # define the list of book which is a value pair of each author key
        if len(books) == 1:     # check if there is only 1 book in the list
            book_to_del = books[0]      # get the first book in the list & define
            delete_confirm = input(f'Do you want to delete the book "{book_to_del}"?\n'
                                   f'Enter \'Y\' to continue or any other key to quit: ').upper()   # ask to confirm
            if delete_confirm == 'Y':
                del readings[author]    # delete the key-value pair from the dictionary
                print(f'"{book_to_del}" by {author} was deleted.\n')
            else:
                print('Okay. Bye!\n')
        elif len(books) > 1:    # check if there are multiple books in the list
            print(f'Book(s) by {author}:')
            print(*books, sep='\n')     # print the list of book without brackets & separate with new line
            book_to_del = no_blank(input('Enter the book title you want to edit: ').title())  # ask which book to delete
            if book_to_del not in books:
                print(f'There is no book titled "{book_to_del}" in the list. Try again!\n')
            else:
                books.remove(book_to_del)   # remove the book from the book list
                print(f'The book "{book_to_del}" was deleted.\n')
    else:
        print(f'There is no book by "{author}" in the list.\n')


def no_blank(user_input):    # a function to avoid blank space as valid input
    while not user_input.strip():   # set a loop if the user input is blank
        user_input = input('Please enter text: ')
    else:
        return user_input


if __name__ == '__main__':
    main()
