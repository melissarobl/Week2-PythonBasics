# When the publish method is called, print an error message if the book given has the same name as a book currently in the books list.
# Do not add the duplicate book. (In other words, make sure the Author object's book list doesn't already contain that name).

class Author:
    def __init__(self, name): #Author has a name and list of books published
        self.name = name
        self.books = [] # empty list of books

    def publish(self, title): # takes the title of a book as an argument.
        if title not in self.books:
            self.books.append(title) # Add title of book to this object's books list


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
   author.publish('Marina') # testing to make sure duplicates don't get added

   print(author)


main()