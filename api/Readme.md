# GraphQL
https://www.twilio.com/blog/graphql-apis-django-graphene

## Query (GraphQL auto convert python Snake to Camal, all_books to allBooks)
http://127.0.0.1:8000/graphql

query {
  allBooks {
    id
    title
    author
    yearPublished
    review
  }
}

query {
  book(bookId: 2) {
    id
    title
    author
  }
}

## Create a book
mutation createMutation {
  createBook(bookData: {title: "Things Apart", author: "Chinua Achebe", yearPublished: "1985", review: 3}) {
    book {
      title,
      author,
      yearPublished,
      review
    }
  }
}

## Update an existing book
mutation updateMutation {
  updateBook(bookData: {id: 6, title: "Things Fall Apart", author: "Chinua Achebe", yearPublished: "1958", review: 5}) {
    book {
      title,
      author,
      yearPublished,
      review
    }
  }
}

## Deleting a book
mutation deleteMutation{
  deleteBook(id: 6) {
    book {
      id
    } 
  }
}
