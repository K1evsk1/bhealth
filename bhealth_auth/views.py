from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout as auth_logout
from bhealth_auth.pipeline import create_user
from client.models import Client


def login(request):
    if request.method == 'GET':
        if request.user.is_superuser:
            return HttpResponseRedirect('/admin/')
        if request.user.is_authenticated():
            return HttpResponseRedirect(
                reverse('client:profile',
                        kwargs={'pk': get_object_or_404(Client, unique_id=request.user.client.unique_id).pk}
                        )
            )

        return render(request, 'bhealth_auth/login.html')


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('bhealth_auth:login'))


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        '''
        add form validation check and else
        '''
        create_user(**{'unique_id': username,'password': password})