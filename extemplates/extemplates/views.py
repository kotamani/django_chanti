from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request, 'contact.html')

def tg(request):
    usermail = request.GET['n1']
    return render(request, 'conscc.html', {'k1' :usermail})
