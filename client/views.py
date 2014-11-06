from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from client.models import Client
from client.decorators import profile_access
from django.contrib.auth.models import User

@profile_access
def profile(request, pk):
    client = Client.objects.get(pk=pk)
    return render(request, 'client/profile_base.html', {'client':client})