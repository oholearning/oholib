from django.shortcuts import render 

def homepage(request):
    """Serve Homepage""" 
    return render (request, "home.html", {

    })