from rest_framework import viewsets, filters, generics, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from apps.finance.api.serializers import BalanceSerializer
from apps.finance.api.filters import BalanceFilter
from apps.finance.models import Replenishment


class BalanceModelViewSet(viewsets.ModelViewSet):
    queryset = Replenishment.objects.all()
    serializer_class = BalanceSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    # filterset_fields = ['status', 'description']
    ordering_fields = ['status', 'description']
    filterset_class = BalanceFilter

# from django_filters.rest_framework import DjangoFilterBackend
# from books.api.filters import BookFilter, AuthorFilter, CategoryFilter
# from books.api.serializers import BookSerializer, AuthorSerializer, CategorySerializer
# from books.models import Book, Author, Category
#
#
# class BookModelViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
#     ordering_fields = ['condition', 'title']
#     filterset_class = BookFilter


# class BalanceList(generics.ListCreateAPIView):
#     queryset = Replenishment.objects.all()
#     serializer_class = BalanceSerializer
#
# class BalanceInstanceView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Replenishment.objects.all()
#     serializer_class = BalanceSerializer

