home_books_sum = int(input())
school_books_sum = int(input())
home_books = set()
for i in range(home_books_sum):
    book = str(input())
    home_books.add(book)
for i in range(school_books_sum):
    book = str(input())
    if book in home_books:
        print('yes')
    else:
        print('no')
