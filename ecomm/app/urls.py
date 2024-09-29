from . import views
from django.urls import path

urlpatterns = [
    path("",views.home),
    path("index/    ",views.index),
    path("category/<slug:val>",views.categoryView.as_view(), name="category" ),
]
