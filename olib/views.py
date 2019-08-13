from django.shortcuts import render 
from apps.content.models import (
    Content,
    Resource
)

def homepage(request):
    """Serve Homepage""" 
    contents = {}
    return render (request, "home.html", {
        'contents': contents

    })