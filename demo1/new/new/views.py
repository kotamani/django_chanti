from django.http import HttpResponse

def say_hi(reqest):
    msg = "<h1> Welcome </h1>"
    return HttpResponse(msg)

