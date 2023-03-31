from django_filters import rest_framework as filters

from apps.finance.models import Replenishment


class BalanceFilter(filters.FilterSet):
    class Meta:
        model = Replenishment
        fields = {
            'status': ['icontains', 'exact'],  # filter(title='awda'), filter(title__exact='awda')
            'description': ['gt', 'gte', 'lt', 'lte'],
        }

