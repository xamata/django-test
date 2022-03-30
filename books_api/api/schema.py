import graphene
from graphene_django import DjangoObjectType, DjangoListField
from .models import Book


# adpats the book Book model to a DjangoObjectType
class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = "__all__"  # indicates that we want all fields in the model available in our API


# Query class provides the queries that will be provided to the clients
class Query(graphene.ObjectType):
    # returns a list of all the book types
    all_books = graphene.List(BookType)
    # returns an instance of one book type
    book = graphene.Field(BookType, book_id=graphene.Int())

    # resolve methods map to the schema
    # two query resolvers query the database using the Django model
    # to execute the query and return the results.
    def resolve_all_books(self, info, **kwargs):
        return Book.objects.all()

    def resolve_book(self, info, book_id):
        return Book.objects.get(pk=book_id)


# similar to Book model so that client can add or change through API
class BookInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    author = graphene.String()
    year_published = graphene.String()
    review = graphene.Int()


class CreateBook(graphene.Mutation):
    # for every mutation class, we have a argument class
    # and a mutate class method
    class Arguments:
        book_data = BookInput(required=True)

    book = graphene.Field(BookType)

    # mutator to add to the database
    @staticmethod
    def mutate(root, info, book_data=None):
        book_instance = Book(
            title=book_data.title,
            author=book_data.author,
            year_published=book_data.year_published,
            review=book_data.review,
        )
        book_instance.save()
        # use CreateBook class to save a new book
        return CreateBook(book=book_instance)