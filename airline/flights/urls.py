# Reference URL: https://www.youtube.com/watch?v=vzGllw18DkA&t=257s - 6:35:16

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:flight_id>", views.flight, name="flight")
]