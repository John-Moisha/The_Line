from django.urls import path
from django.contrib.auth.views import LogoutView
# from ..api.views import BalanceList, BalanceInstanceView
from rest_framework.routers import DefaultRouter
from apps.finance.api import views


app_name = 'finance-api'

# urlpatterns = [
#
#     # path('api/v1/list/', BalanceList.as_view()),
#     # path('api/v1/list/<int:pk>', BalanceInstanceView.as_view()),
#
# ]

router = DefaultRouter()
router.register('balances', views.BalanceModelViewSet, basename='balance')
urlpatterns = router.urls
