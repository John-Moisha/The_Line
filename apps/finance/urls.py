"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views as view

# app_name = 'finance'

urlpatterns = [

    # path('login/', view.LogInView.as_view(), name='login'),
    # path('signup/', view.SignUpView.as_view(), name='signup'),
    #
    # path('logout/', LogoutView.as_view(), name='logout'),

    path('balance/', view.FinanceView.as_view(), name='balance'),
    path('amountin/', view.AmountInView.as_view(), name='amountin'),
    path('amountout/', view.AmountOutView.as_view(), name='amountout'),
    path('finbalance/', view.FinanceBalance.as_view(), name='finbalance'),



    # path('api/v1/list/', view.FinanceApiView.as_view(), name='api-balance'),




]
