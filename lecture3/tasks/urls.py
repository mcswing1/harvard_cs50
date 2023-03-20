# Reference URL: https://www.youtube.com/watch?v=vzGllw18DkA&t=257s - 5:02:26
from django.urls import path

# "." = Import from the current directory the "views.py" file 
from . import views

# Add an app_name field to help uniquely identify URLs tied to the application - 5:19:00
app_name = "tasks"

urlpatterns = [
    path("", views.index, name="index"),
    # Add a new path for the add.html file
    path("add", views.add, name="add")
]