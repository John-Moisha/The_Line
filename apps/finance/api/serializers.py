from rest_framework import serializers

# from books.models import Book, Author, Category
from ..models import Replenishment


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Replenishment
        fields = (
            # 'id',
            'user',
            'description',
            'amount',
            'status',
        )

