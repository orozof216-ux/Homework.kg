from django.views.generic import CreateView, ListView, View
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout

from .forms import RegisterForm, ResumeForm, LoginForm
from .models import Resume


class RegisterView(View):

    def get(self, request):
        user_form = RegisterForm()
        resume_form = ResumeForm()

        return render(request, 'resume/register.html', {
            'user_form': user_form,
            'resume_form': resume_form
        })

    def post(self, request):
        user_form = RegisterForm(request.POST)
        resume_form = ResumeForm(request.POST, request.FILES)

        if user_form.is_valid() and resume_form.is_valid():
            user = user_form.save()

            resume = resume_form.save(commit=False)
            resume.user = user
            resume.save()

            login(request, user)
            return redirect('resume_list')

        return render(request, 'resume/register.html', {
            'user_form': user_form,
            'resume_form': resume_form
        })


class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'resume/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('resume_list')

        return render(request, 'resume/login.html', {'form': form})


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('login')


class ResumeListView(ListView):
    model = Resume
    template_name = 'resume/resume_list.html'
    context_object_name = 'resumes'