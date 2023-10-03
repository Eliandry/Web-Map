from django.shortcuts import render
from django.http import HttpResponse
from .models import Country
from django.contrib import auth

def main(request):
    country = Country.objects.order_by("-population")
    context={'country':country,'username': auth.get_user(request).username}
    return render(request,"index.html",context)