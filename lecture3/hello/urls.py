# Reference URL: https://www.youtube.com/watch?v=vzGllw18DkA&t=257s - 4:22:53
from django.urls import path

# "." = Import from the current directory the "views.py" file 
from . import views

urlpatterns = [
    # References "views.py" file and accesses the index function. 
    # Optionally provide a name with a string to allow for easy reference from other parts of the application. 
    # path("") defines the default route for the app. 
    path("", views.index, name = "index"),
    # New URL path that works with the new view function "mo" created in "views.py" for displaying "Hello, Mo!"
    path("mo", views.mo, name = "mo"),
    # New URL path that matches any string name, will call the greet function and will pass in the name as an argument to the greet function. 
    path("<str:name>", views.greet, name = "greet")
]