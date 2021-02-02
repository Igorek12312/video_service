from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import Http404, HttpResponseRedirect
from .forms import RegistrationForm, UserEditForm
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            context = {'username': username, 'errors': True}
            return render(request, 'index.html', context)
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            user = auth.authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])

            if user:
                auth.login(request, user)
                return HttpResponseRedirect('/')

            return HttpResponseRedirect('/')
        context = {'form': form}
        return render(request, 'registration.html', context)
    context = {'form': RegistrationForm()}
    return render(request, 'registration.html', context)


@login_required()
def edit_user(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/user/edit/')
        context = {'form': form}
        return render(request, 'edit_user.html', context)
    form = UserEditForm(instance=request.user)
    context = {'form': form}
    return render(request, 'edit_user.html', context)

