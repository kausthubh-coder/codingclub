from django.shortcuts import render
from .models import session

# Create your views here.
def index(request):
    data = session.objects.all()
    return render(request,"session/index.html",{"sessions":data})

def sessionpost(request,id):
    postid = id
    data = session.objects.filter(id=postid)
    return render(request,"session/session.html",{"sessions":data})

def sessionquery(request):
    query = request.GET.get('q')
    data = session.objects.filter(title__icontains=query)
    return render(request,"session/index.html",{"sessions":data})

