from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView,
    TemplateView, View, DetailView, FormView)
from apps.accounts.models import CustomUser
from apps.accounts.forms import SettingsForm
from core import settings
# from .forms import CheckForm, VerificationForms, VerifAccountForms,VerificationFormsSet
# from .models import Check, Transaction, Verification


class ReferralView(LoginRequiredMixin, TemplateView):
    # model = CustomUser
    template_name = 'dashboard/referral.html'