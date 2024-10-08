class Author:
    def __init__(self, name): #Author has a name and list of books published
        self.name = name
        self.books = [] # empty list of books

    def publish(self, title): # takes the title of a book as an argument.
        self.books.append(title) # Add title of book to this object's books list

    # def __str__(self): # returns a string with author's name, and names of all their book titles
    #     if self.books:
    #         book_list = ', '.join(self.books)
    #     else:
    #         book_list = 'No books'
    #     return f'Name: {self.name}. Books Published: {book_list}'


    def __str__(self): # returns a string with author's name, and names of all their book titles
      titles = ', '.join(self.books) or 'No published books'
      return f'Name: {self.name}. Books Published: {titles}'


# write a main function to test your class, create some example authors, and publish come example books

def main():
   author = Author('Homer Simpson')
   author.publish('Doh')
   print(author)

   author = Author('Ruiz')
   author.publish('The Shadow of the Wind')
   author.publish('Marina')
   print(author)


main()



# homer_simpson = Author('Homer Simpson')
# homer_simpson.publish('Doh, a book of exclamations')
# homer_simpson.publish('Working at the Nuclear Plant')
#
# print(homer_simpson)
#
#
# clara = Author('Clara')
# print(clara)
