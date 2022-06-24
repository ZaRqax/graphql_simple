import graphene

from products.models import Book, Category, Grocery
from products.schemes.book import BookType
from products.schemes.category import CategoryType
from products.schemes.grocery import GroceryType


class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    books = graphene.List(BookType)
    groceries = graphene.List(GroceryType)

    def resolve_books(root, info, **kwargs):
        # Querying a list
        return Book.objects.all()

    def resolve_categories(root, info, **kwargs):
        # Querying a list
        return Category.objects.all()

    def resolve_groceries(root, info, **kwargs):
        # Querying a list
        return Grocery.objects.all()

schema = graphene.Schema(query=Query)
