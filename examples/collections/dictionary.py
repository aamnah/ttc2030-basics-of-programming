# Key-value pair collection
# like objects in JavaScript

books_dictionary = {
  # key can be a string as well
  # keys can be mismatched as well, but they SHOULD NOT be
  # but they must be UNIQUE
  12345678: 'Book 1',
  '12345679': "Book 2",
  '12345680': "Book 3",
  12345681: "Book 4",
  12345682: "Book 5",
}
print("Contents of the bookdict is:", books_dictionary)


# any date where you have an identifier and the identifier is uniuqe
# that's where dictionaries are useful

# instead of giving it a key, give it an index

mybook = books_dictionary[12345681]
print("Book is:", mybook)

my_other_book = books_dictionary.get(12345681) # you can also use the .get() function
print("Other book is:", my_other_book)

# print all keys in the dictionary
for isbn in books_dictionary:
    print(isbn)

# print all values ​​in the dictionary
# loop over .values()
for bookname in books_dictionary.values():
    print(bookname)

# print keys and values ​​in the dictionary
# loop over .items()
for isbn, bookname in books_dictionary.items():
    print(isbn, bookname)


# check if specific key exists in dictionary
if 12345679 in books_dictionary:
    print("12345679 found in books_dictionary")


# add item to dictionary
books_dictionary[422344] = "New Book"
print("Contents of the books_dictionary after adding a new item is:", books_dictionary)
# if key exits, it will update/replace existing value
books_dictionary[422344] = "New New Book"
books_dictionary[422344] = "New New New Book"
print("Contents of the books_dictionary after adding a new item is:", books_dictionary)

remove_this_book = books_dictionary.pop(12345678)
print("Popped book:", books_dictionary)
print("Contents of the books_dictionary after pop is:", books_dictionary)
