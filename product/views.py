from django.shortcuts import render, render_to_response
from product.models import Product
import json


def search(request):
    if request.is_ajax():
        search_text = request.POST['search_text']
        result = Product.objects.filter(name__icontains=search_text)
        return render_to_response('client/product_search.html', {'result':result})