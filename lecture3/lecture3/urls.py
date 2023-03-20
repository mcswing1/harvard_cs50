# Reference URL: https://www.youtube.com/watch?v=vzGllw18DkA&t=257s - 4:24:53

"""lecture3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Runs the default application which is the "admin" application.
    path('admin/', admin.site.urls),
    # Adding the URL paths for the "hello" app. Inside the hello module, include the "urls.py" file. But this also requires to import "include", which is done above. 
    path('hello/', include("hello.urls")),
    # Adding the URL paths for the "newyear" app. - 4:45:38
    path('newyear/', include("newyear.urls")),
    # Adding the URL paths for the "tasks" app. - 5:01:32
    path('tasks/', include("tasks.urls"))
]
