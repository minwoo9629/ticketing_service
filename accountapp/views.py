from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.views import LoginView
from django.http import response
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView

from accountapp.forms import AccountCreationForm


# Create your views here.

# Account Create FBV
# def create(request):
#     if request.method == 'POST':
#         form = AccountCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('home')
#         else:
#             form = AccountCreationForm()
#
#     else:
#         form = AccountCreationForm()
#
#     return render(request, 'accountapp/create.html', {'form': form})

# Account Create CBV
class AccountCreateView(CreateView):
    model = get_user_model()
    form_class = AccountCreationForm
    template_name = 'accountapp/create.html'
    success_url = reverse_lazy('concertapp:list')

    def form_valid(self, form):
        response = super().form_valid(form)        
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)

        return response

    def form_invalid(self, form):
        return super().form_invalid(form)



class AccountLoginView(LoginView):
    template_name = 'accountapp/login.html'

    def form_invalid(self, form):
        response = super().form_invalid(form)
        form.add_error('username', 'ID 또는 PW가 일치하지 않습니다.')
        return response


class AccountInfoView(DetailView):
    model = get_user_model()
    template_name = "accountapp/info.html"
    context_object_name = "target_user"

class AccountDeleteView(DeleteView):
    model = get_user_model()
    template_name = "accountapp/delete.html"
    success_url = reverse_lazy("concertapp:list")
    context_object_name = "target_user"