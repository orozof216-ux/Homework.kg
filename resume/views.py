from django.shortcuts import render, redirect
from .forms import RegisterForm, ResumeForm, LoginForm
from .models import Resume

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


def register_view(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        resume_form = ResumeForm(request.POST, request.FILES)

        if user_form.is_valid() and resume_form.is_valid():
            user = user_form.save()

            resume = resume_form.save(commit=False)
            resume.user = user
            resume.save()

            login(request, user)
            return redirect('resume_list')

    else:
        user_form = RegisterForm()
        resume_form = ResumeForm()

    return render(request, 'resume/register.html', {
        'user_form': user_form,
        'resume_form': resume_form
    })


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('resume_list')

    else:
        form = LoginForm()

    return render(request, 'resume/login.html', {
        'form': form
    })


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def resume_list(request):
    resumes = Resume.objects.all()
    return render(request, 'resume/resume_list.html', {
        'resumes': resumes
    })