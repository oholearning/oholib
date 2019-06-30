from django.shortcuts import render 
from apps.content.models import (
    Content,
    Resource
)

def homepage(request):
    contents = Content.objects.all()[:4]

    """Serve Homepage""" 
    return render (request, "home.html", {
        'contents': contents

    })