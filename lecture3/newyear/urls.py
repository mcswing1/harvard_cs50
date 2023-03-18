# Reference URL: https://www.youtube.com/watch?v=vzGllw18DkA&t=257s - 4:45:50
from django.urls import path

# "." = Import from the current directory the "views.py" file 
from . import views

urlpatterns = [
    path("", views.index, name="index")
]