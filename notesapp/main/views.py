from django.shortcuts import render

# Create your views here.


class note():
    def __init__(self, content):
        self.content = content

def index(request):
    if "notes" not in request.session:
        request.session["notes"] = []
    return render(request, "main/index.html",{
        "notes": request.session["notes"]
    })
        