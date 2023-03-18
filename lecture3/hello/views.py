# Reference URL: https://www.youtube.com/watch?v=vzGllw18DkA&t=257s - 4:21:55
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request): 
    return render(request, "hello/index.html")

def mo(request):
    return HttpResponse("Hello, Mo!")

# This greet function takes an extra parameter and returns an HTTP response of whatever name is plugged-in.
def greet(request, name):
    # Adjusting this function to take advantage of Django's templating capabilities. - 4:38:35
    # An optional 3rd argument, called the context, allows us to provide all of the information that we want to provide to the template.
    # The context provides the template access to a variable called "name" and its value "name.capitalize()"
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })