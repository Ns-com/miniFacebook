from django.shortcuts import render


def home_page(request):
    return render(request,"messenger_page.html")
