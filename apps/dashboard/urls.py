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
from . import views as dashboard_view
from ..packages import views as packages_view
from ..referral import views as referral_view
from ..finance import views as finance_view

app_name = 'dashboard'

urlpatterns = [

    path('home/', dashboard_view.DashboardView.as_view(), name='home'),
    path('settings/', dashboard_view.SettingsView.as_view(), name='settings'),

    path('investing/', packages_view.PackagesView.as_view(), name='packages'),

    path('referral/', referral_view.ReferralView.as_view(), name='referral'),


    # path('invest/', finance_view.FDepInView.as_view(), name='invest'),

    path('finance/', include('apps.finance.urls')),

]
