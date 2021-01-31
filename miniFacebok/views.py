from django.shortcuts import render


def home_page(request):
    return render(request,"facebook_page.html")

def index_page(request):
    return render(request,"index.html")
