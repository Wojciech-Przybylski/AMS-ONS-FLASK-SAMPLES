from application.book import Book


def test_book_search():

    book1 = Book("Lord of the Rings: The Fellowship of the Ring", 500, "123-4-56-789012-3", "fantasy", "J. R. R. Tolkien")
    book2 = Book("Lord of the Rings: Two Towers", 500, "123-4-56-789012-3", "fantasy", "J. R. R. Tolkien")
    book3 = Book("Lord of the Rings: The Return of the King", 500, "123-4-56-789012-3", "fantasy", "J. R. R. Tolkien")
    assert Book.search("J. R. R. Tolkien") == [book1, book2, book3]
    assert Book.search("J. K. Rowling") == []
    assert Book.search("") == []

