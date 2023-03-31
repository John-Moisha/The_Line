from .models import CustomUser
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, RedirectView
from django.contrib.auth.views import LoginView
from .forms import LogInForm, SighUpForm
from django.contrib import messages
# from annoying.functions import get_object_or_None
from django.contrib.auth import views as auth_views


class LogInView(LoginView):
    template_name = 'account/login.html'
    model = CustomUser
    authentication_form = LogInForm
    # form_class = LogInForm
    redirect_authenticated_user = True

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))
    # fields = ('email', 'password')


class SignUpView(CreateView):
    model = CustomUser
    success_url = reverse_lazy('login')
    form_class = SighUpForm
    template_name = 'account/signup.html'





# class ActivateView(RedirectView):
#     pattern_name = 'login'
#
#     def get_redirect_url(self, *args, **kwargs):
#         username = kwargs.pop('username')
#         user = get_object_or_None(User, username=username, is_active=False)
#         if user is not None and default_token_generator.check_token(user, token): # noqa django token
#             user.is_active = True
#             user.save(update_fields=('is_active', ))
#             messages.add_message(self.request, messages.INFO, 'Your account is activated!')
#         return super().get_redirect_url(*args, **kwargs)


    # form_data = request.POST
    # form_class = LoginForm
    #
    # if request.method == 'POST':
    #     form = form_class(form_data)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('books-list')
    # elif request.method == 'GET':
    #     form = form_class()
    #
    # context = {
    #     'title': 'Login',
    #     'form': form,
    # }
    # return render(request, 'login.html', context=context)

