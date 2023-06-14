from django.urls import path
from firstapp import views
urlpatterns=[
    path('first/',views.index),
    path('',views.index)
]