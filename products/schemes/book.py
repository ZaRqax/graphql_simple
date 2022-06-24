from graphene_django import DjangoObjectType

from products.models import Book


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'author',
            'isbn',
            'pages',
            'price',
            'quantity',
            'description',
            'imageurl',
            'status',
            'date_created',
        )