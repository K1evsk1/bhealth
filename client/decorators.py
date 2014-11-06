from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from client.models import Client
from functools import wraps


def profile_access(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        pk = kwargs['pk']
        if request.user.is_authenticated():
            request_unique_id = request.user.client.unique_id
            client_unique_id = get_object_or_404(Client, pk=pk)

            if request_unique_id == client_unique_id:
                return func(request, pk)
            else:
                return func(request, Client.objects.get(unique_id=request_unique_id).pk)

        else:
            return HttpResponseRedirect(reverse('bhealth_auth:login'))
    return wrapper
