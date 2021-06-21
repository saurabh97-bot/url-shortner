from django.shortcuts import render,redirect
import random
import string

from rest_framework.response import Response
from rest_framework import status

from .models import UrlData
from .form import Url
from rest_framework.decorators import api_view
from .serializer import urlserializer

# Create your views here.

# def urlShort(request):
#     if request.method == 'POST':
#         form = Url(request.POST)
#         if form.is_valid():
#             slug = ''.join(random.choice(string.ascii_letters)
#                            for x in range(5))
#             url = form.cleaned_data["url"]
#
#             new_url = UrlData(url=url, short_url=slug)
#             new_url.save()
#             return redirect('/')
#     else:
#         form = Url()
#     data = UrlData.objects.all()
#     context = {
#         'form': form,
#         'data': data
#     }
#     return render(request, 'index.html', context=context)

def urlRedirect(request, short):
    data = UrlData.objects.get(short_url=short)
    return redirect(data.url)

@api_view(['POST'])
def short_url_data(request):
    serial_data = urlserializer(data=request.data)
    slug = ''.join(random.choice(string.ascii_letters)
                   for x in range(5))

    if serial_data.is_valid():
        url = request.data['url']
        data = UrlData(url=url,short_url=slug)
        data.save()
       # serial_data.save()
    return Response('http://127.0.0.1:8000/'+'u/'+str(slug))
