# Reference URL: https://www.youtube.com/watch?v=vzGllw18DkA&t=257s - 4:46:00
import datetime

from django.shortcuts import render

# Create your views here.
def index(request):
    # Create the "now" variable with access to the current date
    now = datetime.datetime.now()
    return render(request, "newyear/index.html", {
        "newyear": now.month == 1 and now.day == 1
    })