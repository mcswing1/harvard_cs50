# Reference URL: https://www.youtube.com/watch?v=vzGllw18DkA&t=257s - 5:02:34
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Add a global variable called "tasks" with a list of tasks to display.
# Changed to an empty list. - 5:37:42
tasks = []

# Define a Python class for the form - 5:26:55
class NewTaskForm(forms.Form):
    # Define all the fields that the form needs to have, all the inputs we want the user to provide
    # User will type in characters into the form and saved to variable "task"
    task = forms.CharField(label="New Task")
    # Indicate the priority of a task and add constraints to ensure the data is valid. This is client-side validation. - 5:28:45
    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", { 
        "tasks": tasks
    })

# Create a new page that will allow us to add new tasks. 
def add(request):
    # Add a condition to process the request. "request.POST" contains all the data the user submitted when they submitted the form. - 5:31:30
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            # Give access to all the data the user submitted.
            task = form.cleaned_data["task"]
            # Add the task to the list of tasks. 
            tasks.append(task)
            # Return the user back to the "tasks" screen after adding a task using the built-in reverse function in Django - 5:36:52
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                # Send back the existing form data if the data is not valid.
                "form": form
            })
    # Add some context to add.html, give the page access to a variable called "form" which will be a NewTaskForm() - 5:27:33
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })