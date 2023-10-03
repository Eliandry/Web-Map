from django.shortcuts import render
from django.http import HttpResponse
from .models import Country


def main(request):
    country = Country.objects.order_by("-population")
    context={'country':country}
    return render(request,"main.html",context)