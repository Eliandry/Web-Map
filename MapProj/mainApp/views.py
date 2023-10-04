from django.shortcuts import render
from django.http import HttpResponse
from .models import Country
from django.contrib import auth


def main(request):
    all_pop_country = Country.objects.order_by("-popular")
    all_like_country = Country.objects.order_by("-grade")
    all_area_country = Country.objects.order_by("-area")
    pop_country = all_pop_country[:8]
    like_country = all_like_country[:8]
    area_country=all_area_country[:8]
    context = {'pop_country': pop_country, 'like_country': like_country,'area_country': area_country, 'username': auth.get_user(request).username}
    return render(request, "main.html", context)
