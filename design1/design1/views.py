from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
def result(request):
    sname = request.GET['n1']
    course = request.GET['n2']
    clist = course.split(' ')
    l=len(clist)
    price = l*5000
    return render(request, 'result.html', {'k1':sname,'k2':clist,'k3':l,'k4':price})