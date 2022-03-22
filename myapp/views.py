from ctypes.wintypes import MSG
from django.shortcuts import render
from myapp.models import Team, Gallery, Msg
from django.views.decorators.csrf import csrf_exempt
# from django.contrib.messages import success
# Create your views here.

def index(request):
    return render(request, 'myapp/index.html')

def about(request):
    return render(request, 'myapp/about.html')

@csrf_exempt
def contact(request):
    if request.method == 'POST':
       name = request.POST.get('name')
       mail = request.POST.get('mail')
       message = request.POST.get('message')
       data = Msg(name = name, email = mail, message = message)
       data.save()
    #    success(request, 'Thank You ! We will contact to you Soon!!')
       return render(request, 'myapp/contact.html')
    else:
       return render(request, 'myapp/contact.html')

def gallery(request):
   data = Gallery.objects.all()
   return render(request, 'myapp/gallery.html', {'data': data})

def team(request):
    data = Team.objects.all()
    return render(request, 'myapp/team.html',{'data':data})

def donate(request):
    return render(request, 'myapp/donate.html')