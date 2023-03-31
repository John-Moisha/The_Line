import json
import time

from django.db.models import Sum
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http import HttpResponse
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
from .forms import AmountForm
from .models import Replenishment


class FinanceBalance(LoginRequiredMixin, TemplateView):
    model = Replenishment
    template_name = 'dashboard/finbalance.html'

    def get_queryset(self):
        # Replenishment.objects.all()
        qs = Replenishment.objects.all()
        qs = qs.filter(user_id=self.request.user.id)
        qs = qs.order_by('-data')
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sum_sum'] = Replenishment.objects.aggregate(Sum('amount'))


        return context


class FinanceView(LoginRequiredMixin, ListView):
    # model = Replenishment
    paginate_by = 10

    # queryset = Replenishment.objects.all()#.filter(user_id=CustomUser.id)
    template_name = 'dashboard/finance.html'

    def get_queryset(self):
        # Replenishment.objects.all()
        qs = Replenishment.objects.all()
        qs = qs.filter(user_id=self.request.user.id)
        qs = qs.order_by('-data')
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sum_in = Replenishment.objects.filter(user_id=self.request.user.id, status='I').aggregate(Sum('amount'))['amount__sum']
        sum_out = Replenishment.objects.filter(user_id=self.request.user.id, status='O').aggregate(Sum('amount'))['amount__sum']

        context['sum_in'] = sum_in
        context['sum_out'] = sum_out
        if sum_in is None:
            context['sum_in'] = 0
        # elif sum_out is None:
        #     context['sum_in'] = 'Вы еще не пополнились'
        elif sum_out is None:
            context['sum_out'] = 0
        else:
            context['sum_sum'] = sum_in-sum_out
        return context



class AmountInView(LoginRequiredMixin, CreateView):
    template_name = 'dashboard/f_form.html'
    success_url = reverse_lazy('dashboard:balance')
    form_class = AmountForm

    def get_initial(self):
        return {
            'user': self.request.user,
        }

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.description = 10
        form.instance.status = 'I'
        return super(AmountInView, self).form_valid(form)


class AmountOutView(LoginRequiredMixin, CreateView):
    template_name = 'dashboard/f_form.html'
    success_url = reverse_lazy('dashboard:balance')
    form_class = AmountForm

    def get_initial(self):
        return {
            'user': self.request.user,
        }

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.description = 20
        form.instance.status = 'O'
        return super(AmountOutView, self).form_valid(form)


# class FinanceApiView(LoginRequiredMixin, View):
#     #
#     # def get_queryset(self):
#     #     queryset = super().get_queryset()
#     #     return queryset.filter(user_id=self.request.user.id)
#
#     def get(self, request):
#         queryset = Replenishment.objects.all().filter(user_id=self.request.user.id)
#         results = [
#             {'id': obj.id, 'user': obj.user.first_name}
#             for obj in queryset
#         ]
#         data = {
#             'result': results
#         }
#         return HttpResponse(json.dumps(data))

# Work!
# class FinanceView(LoginRequiredMixin, ListView):
#     # model = Replenishment
#     queryset = Replenishment.objects.all()
#     template_name = 'dashboard/finance.html'
#
#     # def get_object(self):
#     #     # context = get_object_or_404(Transaction, user_id=self.request.user.id)
#     #     # context['doc'] = self.
#     #     return get_object_or_404(Replenishment, user_id=self.request.user.id)
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         return queryset.filter(user_id=self.request.user.id)
