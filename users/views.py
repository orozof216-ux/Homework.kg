from django.shortcuts import render, redirect 
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView, ListView, View  
from . import models, forms


class RegisterView(CreateView):  
    form_class = forms.CustomRegisterForm  
    template_name = 'users/register.html'   
    success_url = '/users/login/'           


class AuthLoginView(View):  

    def get(self, request):  
        form = AuthenticationForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):  
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/users/')

        return render(request, 'users/login.html', {'form': form})


class AuthLogoutView(View):  
    def get(self, request):
        logout(request)
        return redirect('/users/login/')


class UserListView(ListView):  
    model = models.CustomUser   
    template_name = 'users/user_list.html'  
    context_object_name = 'us'  