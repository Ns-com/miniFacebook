from django.shortcuts import render


def home_page(request):
    return render(request,"facebook_page.html")

def login_page(request):
    return render(request,"login_form.html")


def registration_page(request):
    return render(request,"registration_form.html")

# Just for test

# just random lines
#some more lines
# some more 
